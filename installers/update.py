import os
import shutil
import zipfile
import subprocess
from pathlib import Path
import subprocess

archive_path = os.path.join(os.getcwd(), "btwupdate.zip")
output_folder = "C:\\BTWLauncher"

with zipfile.ZipFile(archive_path, 'r') as zip_ref:
    zip_ref.extractall(output_folder)
    subprocess.Popen(r"C:\BTWLauncher\app\app.exe")
