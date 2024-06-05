import os
import tkinter as tk
import webbrowser

# Главное меню Лаунчера Биг Тейсти Ворлда
# Разработчики: roman.126, 2kfc
# https://bit.ly/btw-mserver

MODS_FILE_PATH = os.path.join(os.path.expanduser("~"), "mods.txt")
VERSION_FILE_PATH = "C://BTWLauncher/version.txt"

def check_mods_content():
    if os.path.exists(MODS_FILE_PATH):
        with open(MODS_FILE_PATH, "r") as mods_file:
            mods_value = mods_file.read().strip()
            if mods_value == "1":
                button3.config(state=tk.DISABLED)

def open_installer():
    os.system('C:\\BTWLauncher\\inst\\installer.exe')
    
def open_html_file():
    file_path = "C:\\BTWLauncher\\sites\\main.html"
    if os.path.exists(file_path):
        webbrowser.open("file://" + file_path)
    else:
        print("HTML файл не найден")

def open_server_info():
    server_info_window = tk.Toplevel()
    server_info_window.title("Айпишник сервера")
    server_info_window.geometry("400x200")
    server_info_window.resizable(False, False)

    title_label = tk.Label(server_info_window, text="Айпишник сервера", font=("Arial", 14))
    title_label.pack(pady=10)

    ip_label = tk.Label(server_info_window, text="BigteystiBigMac.aternos.me:63321", font=("Arial", 12), fg="blue")
    ip_label.pack(pady=5)

    text = """Если вы хотите зайти на сервер, то вам нужно попросить внести ваш никнейм в вайт-лист сервера!"""
    text_label = tk.Label(server_info_window, text=text, font=("Arial", 12), wraplength=380, justify="center")
    text_label.pack(pady=10)

def get_version():
    if os.path.exists(VERSION_FILE_PATH):
        with open(VERSION_FILE_PATH, "r") as version_file:
            return version_file.read().strip()
    return "Версия не найдена"

window = tk.Tk()
window.title("Биг Тейсти Ворлд")
window.geometry("609x369")  
print('Не обращайте внимание на консоль, если ничего плохого не происходит.')
print('Если программа не работает и/или сломалась, обращайтесь сюда:')
print('https://t.me/kobicom https://bit.ly/btw-mserver')

content_frame = tk.Frame(window)
content_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

title_label = tk.Label(content_frame, text="Биг Тейсти Ворлд", font=("Arial", 24))
title_label.pack()  

text = """Добро пожаловать в недо-лаунчер Биг Тейсти Ворлда!
Тут расположена вся нужная информация, которая может тебе понадобится!"""
text_label = tk.Label(content_frame, text=text, font=("Arial", 14), wraplength=550, justify="center")
text_label.pack(pady=20)

def open_discord():
    webbrowser.open("https://bit.ly/btw-mserver")
    window.destroy()

button_frame = tk.Frame(content_frame)
button_frame.pack()

button1 = tk.Button(button_frame, text="Информация", command=open_html_file, font=("Arial", 14))
button1.pack(side=tk.LEFT, padx=10) 

button2 = tk.Button(button_frame, text="Discord-сервер", command=open_discord, font=("Arial", 14))
button2.pack(side=tk.LEFT, padx=10) 

button3 = tk.Button(button_frame, text="Установить моды", command=open_installer, font=("Arial", 14))
button3.pack(side=tk.LEFT, padx=10)  

server_button = tk.Button(window, text="Айпи сервера", command=open_server_info, font=("Arial", 14))
server_button.place(relx=0.79, rely=0.75, anchor=tk.CENTER)

version_label = tk.Label(window, text="Версия: " + get_version(), font=("Arial", 12))
version_label.place(x=15, y=352, anchor=tk.SW)

window.resizable(False, False)

check_mods_content()

window.mainloop()
