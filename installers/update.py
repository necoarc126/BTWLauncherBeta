import os
import zipfile
import subprocess
import ctypes

archive_path = os.path.join(os.getcwd(), "btwupdate.zip")
output_folder = "C:\\BTWLauncher"

def show_message(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x0)

def update_and_launch():
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
        show_message("Обновление", "Обновление завершено!")
        subprocess.Popen([r"C:\BTWLauncher\app\app.exe"], shell=True)
    except Exception as e:
        show_message("Ошибка", f"Произошла ошибка: {str(e)}")

update_and_launch()
