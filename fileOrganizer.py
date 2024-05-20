import os
from pathlib import Path
import shutil
import schedule
import time


def Organizer():
    home_directory = os.path.expanduser('~')
    os.chdir(f"{home_directory}/Downloads")
    images = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".tiff")
    audio = (".mp3", ".wav")

    print("Running Script")

    # searches through files in downloads directory and organizes them based on file extension
    for file in os.listdir():
        f = Path(file)
        name, ext = f.stem, f.suffix
        
        if ext in images:
            shutil.move(f"{home_directory}/Downloads/{f}", f"{home_directory}/Pictures")
        if ext == ".pdf":
            shutil.move(f"{home_directory}/Downloads/{f}", f"{home_directory}/Documents")

# use python scheduler to run every 1 minute
schedule.every(1).minutes.do(Organizer)

while True:
    schedule.run_pending()
    time.sleep(1)
#Organizer()