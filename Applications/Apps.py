import os
import time
import sys
import shutil
import subprocess
import getpass
import platform
import urllib
import platform

arch = platform.machine().lower()

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(r"""
                              
███████╗██╗   ██╗██╗     ██╗     
██╔════╝██║   ██║██║     ██║     
█████╗  ██║   ██║██║     ██║     
██╔══╝  ██║   ██║██║     ██║     
██║     ╚██████╔╝███████╗███████╗
╚═╝      ╚═════╝ ╚══════╝╚══════╝
                                                          
""")

user = getpass.getuser()

print(f"\nHello {user}! This Script Is An Automation Program Meant To Install Some Things For You So Your System Is Ready As A User!")
confirm = input("\nContinue? (yes/no) ")

if confirm.lower() != "yes":
    print("Okay, If You Change Your Mind, Just Re-Run And Type `yes` !")
    sys.exit(1)
if platform.system() == "Windows":
    if shutil.which("winget"):
        os.system('winget install Vencord.Vesktop --silent --accept-source-agreements --accept-package-agreements')
        os.system('winget install Spotify.Spotify --silent --accept-source-agreements --accept-package-agreements')
        os.system('cls')
        print("Okay! That's It! All I Did Was Install Vesktop And Spotify!")
        sys.exit(1)
    else:
        os.system('cls')
        print("Winget Not Found!")
        sys.exit(1)
elif platform.system() == "Linux":
    if shutil.which("pacman"):
        if shutil.which("yay"):
            print("\nInstalling Spotify & Vesktop!")
            subprocess.run([
                "yay", "-S", "spotify", "vesktop", "--noconfirm"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif shutil.which("paru"):
            print("\nInstalling Spotify & Vesktop!")
            subprocess.run([
                "paru", "-S", "spotify", "vesktop", "--noconfirm"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print("Supported AUR Helpers Not Found!")
            sys.exit(0)
        sys.exit(1)
    elif shutil.which("apt"):
        os.system("curl -sS https://download.spotify.com/debian/pubkey_5384CE82BA52C83A.asc | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg")
        os.system('echo "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list')
        subprocess.run([
            "sudo", "apt-get", "update", "-y", "&&", "sudo", "apt-get", "install", "spotify-client", "-y"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if arch in ['x86_64', 'amd64']:
            url = "https://vencord.dev/download/vesktop/amd64/deb"
            file_name = "Vesktop_AMD64.deb"
            urllib.request.urlretrieve(url, file_name)
            subprocess.run([
                "sudo", "apt", "install", "Vesktop_AMD64.deb"
            ])
        elif arch in ['aarch64', 'arm64']:
            url = "https://vencord.dev/download/vesktop/arm64/deb"
            file_name = "Vesktop_Arm64.deb"
            urllib.request.urlretrieve(url, file_name)
            subprocess.run([
                "sudo", "apt", "install", "Vesktop_Arm64.deb"
            ])
        else:
            print(f"Unknown architecture: {arch}")
            sys.exit(0)
    elif shutil.which("dnf"):
        subprocess.run([
            "sudo", "dnf", "copr", "enable", "jeffpeng3/vesktop"
        ])
        subprocess.run([
            "sudo", "dnf", "install", "vesktop"
        ])
        os.system('clear')
    else:
        os.system('clear')
        print("No Supported Package Manager Found!")
        sys.exit(1)
else:
    print("Currently Unsupported Operating System!")
    sys.exit(1)