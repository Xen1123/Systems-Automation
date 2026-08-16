import os
import platform
import getpass
import shutil
import sys
import subprocess
from pathlib import Path

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(r"""

 ██████╗██╗     ███████╗ █████╗ ███╗   ██╗    ██╗   ██╗██████╗ 
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║    ██║   ██║██╔══██╗
██║     ██║     █████╗  ███████║██╔██╗ ██║    ██║   ██║██████╔╝
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║    ██║   ██║██╔═══╝ 
╚██████╗███████╗███████╗██║  ██║██║ ╚████║    ╚██████╔╝██║     
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝     
                                                                         
""")
user = getpass.getuser()
print(f"Hello {user}! This Script Is An Automation Program Meant To Clean Your System Of Unnecessary Files And Folders To Free Up Space!")
confirm = input("Continue? (yes/no) ")
if confirm.lower() != "yes":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    sys.exit()
if platform.system() == "Windows":
    print("Cleaning Windows temporary files and flushing DNS...")

    subprocess.run(["ipconfig", "/flushdns"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    
    temp_dir = os.environ.get('TEMP')
    if temp_dir and os.path.exists(temp_dir):
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception:
                pass
elif platform.system() == "Linux":
    if shutil.which("apt"):
        os.system("sudo apt autoremove -y && sudo apt autoclean -y && sudo apt clean -y")
    elif shutil.which("pacman"):
        os.system("sudo pacman -Sc --noconfirm")
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        conf = input("Remove package cache files? They aren't needed typically, but good to keep before a big update! (y/n) ")
        if conf.lower() != "y":
            print("Skipping!")
            pass
        if conf.lower() == "y":
            os.system("sudo pacman -Sc --noconfirm")
    elif shutil.which("dnf"):
        os.system("sudo dnf autoremove -y && sudo dnf clean all -y")
    else:
        print("No Supported Package Manager Found!")
        sys.exit(1)
    os.system("sudo rm -rf ~/.cache/*")
    os.system("sudo rm -rf ~/.local/share/Trash/*")
    os.system("sudo rm -rf /var/cache/*")
    os.system('clear')
elif platform.system() == "Darwin":
    os.system("sudo rm -rf ~/Library/Caches/*")
    os.system("sudo rm -rf ~/Library/Logs/*")
    os.system("sudo rm -rf ~/Library/Application Support/CrashReporter/*")
    os.system("sudo rm -rf /Library/Caches/*")
    os.system("sudo rm -rf /System/Library/Caches/*")
    os.system('clear')
else:
    print("Currently Unsupported Operating System!")
    sys.exit()
print("Okay! That's It! Your System Should Be Cleaned Up Now!")
sys.exit(1)