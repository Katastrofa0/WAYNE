# СНИМОК ЭКРАНА ЦЕЛИ НА СВОЙ ТЕЛЕГРАМ БОТ
![Image alt](https://github.com/Katastrofa0/WAYNE/blob/cc3f92e112e50f9d5928213381bbab36e3a93a45/wayne.png)



ФУНКЦИИОНАЛ:

При запуске, утилита прописывается в авторан и создаётся копия файла, на случай, если цель удалит оригинал. 
В авторан добавляется копия, созданная при первом запуске, расположенная по умолчанию в директории C:\\Wayne.exe.
Там же создаётся маркер, который при перезапуске ПК, сообщает о том, что утилита уже работает.
Утилита проста в использовании и пока не детектится WinDefender . 

Команды:
- /screen : Присылает скриншот текущего экрана жертвы
- /ip : Получить IP
- /sysinfo : Получить инфо о системе



<b>ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ</b> : 
1. Создайте телеграм бота, получите и вставьте свой API ключ 
2. Если требуется, замените название файла, путь её копирования, маркер (всё указано в скрипте) 
3. Если нужен .exe файл, то "скомпилируйте" скрипт через pyinstaller : `pyinstaller --onefile --noconsole wayne.py`
4. Доставить на целевой хост и принудить к исполнению файла.



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
<em>Утилита только для учебных целей!! Автор не несёт никакой ответсвенности за использование в нелегальных целях. 
Создано с целью показать вариант события, запустив непонятный файл.</em>

