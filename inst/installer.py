import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import threading
import time
import subprocess

# Установщик модов Биг Тейсти Ворлда
# Разработчики: roman.126, 2kfc
# https://bit.ly/btw-mserver

MODS_FILE_PATH = os.path.join(os.path.expanduser("~"), "C:\\BTWLauncher\inst\mods.txt")

def check_mods_file():
    if os.path.exists(MODS_FILE_PATH):
        with open(MODS_FILE_PATH, "r") as mods_file:
            mods_value = mods_file.read().strip()
            if mods_value == "1":
                messagebox.showinfo("Моды уже установлены", "Моды уже установлены!")
                root.destroy()

def extract_archive_and_create_mods_file(archive_path, output_dir):
    try:
        with zipfile.ZipFile(archive_path, "r") as zip_ref:
            zip_ref.extractall(output_dir)

        with open(MODS_FILE_PATH, "w") as mods_file:
            mods_file.write("1")

        messagebox.showinfo("Успех", "Моды успешно установлены! Для корректной работы основной программы, ее нужно перезагрузить.")

        subprocess.run(["taskkill", "/F", "/IM", "app.exe"])
        subprocess.run(["taskkill", "/F", "/IM", "installer.exe"])

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}\nОткат изменений...")
        shutil.rmtree(output_dir, ignore_errors=True)

def select_folder_and_install_mods():
    global output_dir
    output_dir = filedialog.askdirectory(title="Выберите корневую папку Minecraft")
    if output_dir:
        path_label.config(text="Найден путь!", fg="green")
        select_path_button.config(state=tk.DISABLED)
        install_button = tk.Button(root, text="Начать установку", command=install_mods)
        install_button.pack(pady=20)

def install_mods():
    progress_window()
    t = threading.Thread(target=extract_archive_and_create_mods_file, args=("C://BTWLauncher/inst/assets/data.zip", output_dir))
    t.start()

def progress_window():
    progress_window = tk.Toplevel()
    progress_window.title("Установка модов")
    progress_window.geometry("300x100")
    progress_label = tk.Label(progress_window, text="Установка модов...")
    progress_label.pack(pady=20)

    time.sleep(5)

    progress_window.destroy()

root = tk.Tk()
root.title("Установка модов Minecraft")
root.geometry("400x200")
root.resizable(False, False)
print('Не обращайте внимания на консоль, если ничего плохого не происходит.')
print('Если программа не работает и/или сломалась, обращайтесь сюда:')
print('https://t.me/kobicom https://bit.ly/btw-mserver')

title_label = tk.Label(root, text="Выберите корневую папку Minecraft", font=("Arial", 14))
title_label.pack(pady=20)

select_path_button = tk.Button(root, text="Выбрать путь...", command=select_folder_and_install_mods)
select_path_button.pack()

path_label = tk.Label(root, text="", font=("Arial", 12))
path_label.pack(pady=10)

check_mods_file()

root.mainloop()
