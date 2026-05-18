import shutil, os, subprocess, sys, getpass
from pathlib import Path

def organize(path):
    extension_map = {
        '.jpg': 'Images',
        '.png': 'Images',
        '.pdf': 'Documents',
        '.txt': 'Documents',
        '.mp4': 'Videos',
        '.mp3': 'Music/Audio',
        '.py':  'Scripts',
        '.sh': 'Scripts',
        '.bat': 'Scripts'
    }

    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)

        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            if ext in extension_map:
                target_dir = os.path.join(path, extension_map[ext])

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.move(filepath, os.path.join(target_dir), filename)
                print(f"Moved: {filename} -> {extension_map[ext]}/")

organize('./')