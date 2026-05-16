import os
import platform
import getpass
import shutil
import sys
import subprocess
from pathlib import Path

print(r"""

 ██████╗██╗     ███████╗ █████╗ ███╗   ██╗
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║
██║     ██║     █████╗  ███████║██╔██╗ ██║
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║
╚██████╗███████╗███████╗██║  ██║██║ ╚████║
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                          
""")
user = getpass.getuser()
print(f"Hello {user}! This Script Is An Automation Program Meant To Clean Your System Of Unnecessary Files And Folders To Free Up Space!")
confirm = input("Continue? (yes/no) ")
if confirm.lower() != "yes":
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
        os.system("sudo rm -rf /var/cache/pacman/pkg/*")
    elif shutil.which("dnf"):
        os.system("sudo dnf autoremove -y && sudo dnf clean all -y")
    else:
        print("No Supported Package Manager Found!")
        sys.exit(1)
    os.system("rm -rf ~/.cache/*")
    os.system("rm -rf ~/.local/share/Trash/*")
    os.system("rm -rf /var/cache/*")
    os.system('clear')
elif platform.system() == "Darwin":
    os.system("rm -rf ~/Library/Caches/*")
    os.system("rm -rf ~/Library/Logs/*")
    os.system("rm -rf ~/Library/Application Support/CrashReporter/*")
    os.system("rm -rf /Library/Caches/*")
    os.system("rm -rf /System/Library/Caches/*")
    os.system('clear')
else:
    print("Currently Unsupported Operating System!")
    sys.exit()
print("Okay! That's It! Your System Should Be Cleaned Up Now!")
sys.exit(1)