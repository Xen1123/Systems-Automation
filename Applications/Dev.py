import getpass
import os
import platform
import shutil
import subprocess
import sys
import time

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

print(r"""

██████╗ ███████╗██╗   ██╗
██╔══██╗██╔════╝██║   ██║
██║  ██║█████╗  ██║   ██║
██║  ██║██╔══╝  ╚██╗ ██╔╝
██████╔╝███████╗ ╚████╔╝
╚═════╝ ╚══════╝  ╚═══╝

""")

user = getpass.getuser()

print(
    f"Hello {user}! This Script Is An Automation Program Meant To Install Some Things For You So Your System Is Ready As A Developer!"
)
confirm = input("Continue? (y/n) ")

if confirm.lower() != "y":
    print("Okay, If You Change Your Mind, Just Re-Run And Type `yes` !")
    sys.exit(1)
if platform.system() == "Windows":
    if shutil.which("winget"):
        os.system(
            "winget install Git.Git --silent --accept-source-agreements --accept-package-agreements"
        )
        os.system(
            "winget install Google.PlatformTools --silent --accept-source-agreements --accept-package-agreements"
        )
        os.system(
            "winget install ZedIndustries.Zed --silent --accept-source-agreements --accept-package-agreements"
        )
        os.system(
            "winget install 0x192.UniversalAndroidDebloaterGUI --silent --accept-source-agreements --accept-package-agreements"
        )
        os.system("cls")
        print(
            "Okay! That's It! All I Did Was Install Git, ADB & Fastboot, VSCode, And The Universal Android Debloater GUI!"
        )
        sys.exit(1)
    else:
        os.system("cls")
        print("Winget Not Found!")
        sys.exit(1)
elif platform.system() == "Linux":
    if shutil.which("pacman"):
        os.system(
            "sudo pacman -S zed android-tools base-devel git --needed --noconfirm"
        )
        os.system("clear")
    elif shutil.which("apt"):
        os.system("sudo apt install adb fastboot git snapd -y")
        os.system("sudo systemctl enable --now snapd.socket")
        os.system("sudo snap install code --classic -y")
        os.system("clear")
    elif shutil.which("dnf"):
        os.system("sudo dnf install android-tools git code -y")
        os.system("clear")
    else:
        os.system("clear")
        print("No Supported Package Manager Found!")
        sys.exit(1)
else:
    print("Currently Unsupported Operating System!")
    sys.exit(1)
