<pre>
🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜
🟦🟦🟦🟦🟦🟦⬜🟥🟥🟥🟥🟥🟥
🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜
⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
</pre>
#EN

A script for auto-restart scripts is what many developers are missing.
One day I needed to automatically restart scripts on the server (since Telegram bots, after updating via my [autoupdate](https://github.com/sekalYT/autoupdategit), require a reboot for the changes to take effect)
And then I thought, why don’t I write my own auto-restart script?

❓ How does it work?

* Place the script in the location where the main.py file is located. (that is, they must be in the same place)
* Run the script using "python autorestart.py"
* Enjoy!

📃 Notes:

* forceupdate - restart the script without waiting time.
* countdown - time until the next scheduled restart.

🛠️ Settings:

The script contains the #settings location. Current variables will appear below it, in which you can specify the time of your restart (for example, restarthour = 22 -> restart will occur at 22:00)
You can change hours, minutes, seconds and microseconds (I don't know what you need them for)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<pre>
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
</pre>
#RU 

Скрипт для автоперезапуска - вот чего не хватает многим разработчикам.
Однажды мне понадобилось автоматически перезапускать скрипты на сервере (так как Telegram боты после обновления через мой [autoupdate](https://github.com/sekalYT/autoupdategit) требует перезагрузки для того, чтобы изменения вступили в силу)
И тогда я подумал, а почему бы мне не написать свой собственный скрипт автоперезапуска?

❓ Как это работает?

* Расположите скрипт в месте, где находится main.py файл. (то есть они должны находиться в одном месте)
* Запустите скрипт с помощью "python autorestart.py"
* Готово!

📃 Команды:

* forceupdate - перезапуск скрипта без ожидания времени.
* countdown - время до следующего запланированного перезапуска.

🛠️ Доп. Настройка:

В скрипте прописано место #settings. Под ним находятся строки-переменные, в которых можно указать время вашего перезапуска (например restarthour = 22 -> перезапуск произойдёт в 22:00)
Вы можете изменять часы, минуты, секунды и микросекунды (не знаю для чего они вам)
