import os
import subprocess
import asyncio
from datetime import datetime, timedelta

# settings
restarthour = 0  # default = 0
restartminute = 0  # default = 0
restartsecond = 0  # default = 0
restartmicrosecond = 0  # default = 0

relative_path_to_main = r'main.py'

main_script = os.path.join(os.path.dirname(__file__), relative_path_to_main)

seconds_until_restart = None

def get_seconds_until_restart():
    now = datetime.now()
    next_restart = now.replace(hour=restarthour, minute=restartminute, second=restartsecond, microsecond=restartmicrosecond)
    if next_restart <= now:
        next_restart += timedelta(days=1)
    return (next_restart - now).total_seconds()

async def update_seconds_until_restart():
    global seconds_until_restart
    while True:
        seconds_until_restart = get_seconds_until_restart()
        await asyncio.sleep(1)

async def restart_main_script():
    global seconds_until_restart
    process = await asyncio.create_subprocess_exec('python', main_script)
    print(f'Started main.py with PID {process.pid}')
    
    try:
        while True:
            seconds_until_restart = get_seconds_until_restart()
            print(f'Sleeping for {seconds_until_restart:.2f} seconds until the next restart')
            await asyncio.sleep(seconds_until_restart)
        
            print('Restarting main.py')
            process.terminate()
            await process.wait()
            process = await asyncio.create_subprocess_exec('python', main_script)
            print(f'Started main.py with PID {process.pid}')
    except asyncio.CancelledError:
        print('Terminating the script due to CancelledError')
        process.terminate()
        await process.wait()

async def command_listener():
    global seconds_until_restart
    while True:
        command = await asyncio.get_event_loop().run_in_executor(None, input)
        if command.strip().lower() == 'countdown':
            if seconds_until_restart is not None:
                hours, remainder = divmod(seconds_until_restart, 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f'Until restart: {int(hours):02}:{int(minutes):02}:{int(seconds):02}')
            else:
                print('Unable to determine the time until the next restart.')
        elif command.strip().lower() == 'forcerestart':
            print('Forcing restart of main.py')
            os.system(f'python {main_script}')

async def main():
    task1 = asyncio.create_task(restart_main_script())
    task2 = asyncio.create_task(update_seconds_until_restart())
    task3 = asyncio.create_task(command_listener())
    
    await task1
    await task2
    await task3

if __name__ == "__main__":
    asyncio.run(main())