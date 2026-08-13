import getpass, os, platform, shutil, sys, time, subprocess

def clear()
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
print(f"Hello {user}! This script will allow you to quickly install some apps that are considered necessary for the typical user!")
time.sleep(2)

keepgoing = input("Continue? (y/n) ")
if keepgoing.lower() == y:
     if shutil.which("winget"):

        # GIT

        gitconfirm = input("Install Git? (y/n) ")
        if gitconfirm.lower() == y:
            print("\nInstalling Git!")
            git_fail = subprocess.run(["winget", "install", "Git.Git", "--silent", "--accept-source-agreements", "--accept-package-agreements"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, capture_output=True, text=True)
            if git_fail.returncode != 0:
                print("Git installation failed!")
                time.sleep(2)
            elif git_fail.returncode == 0:
                pass
        elif gitconfirm.lower() != y:
            clear()
            pass

        # ADB & FASTBOOT

        afconfirm = input("Install ADB & Fastboot? (y/n) ")
        if afconfirm.lower() == y:
            print("Installing ADB & Fastboot!")
            af_fail = subprocess.run(["winget", "install", "Google.PlatformTools", "--silent", "--accept-source-agreements", "--accept-package-agreements"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, capture_output=True, text=True)
            if af_fail.returncode != 0:
                print("ADB & Fastboot not installed!")
                time.sleep(2)
            elif af_fail.returncode == 0:
                pass
        elif afconfirm.lower() != y:
            clear()
            pass

        # VISUAL STUDIO CODE (VSCODE)

        vsconfirm = input("Install Visual Studio Code? (y/n) ")
        if vsconfirm.lower() == y:
            print("Installing VSCode!")
            vsfail = subprocess.run(["winget", "install", "Microsoft.VisualStudioCode", "--silent", "--accept-source-agreements", "--accept-package-agreements"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, capture_output=True, text=True)
            if vsfail.returncode != 0:
                print("VSCode not installed!")
                time.sleep(2)
            elif vsfail.returncode == 0:
                pass
        elif vsconfirm.lower() != y:
            clear()
            pass

        # SSH

        sshconfirm = input("Install SSH? (y/n) ")
        if sshconfirm.lower() == y:
            print("Installing SSH!")
            sshfail = subprocess.run(["winget", "install", "Microsoft.OpenSSH.Beta", "--silent", "--accept-source-agreements", "--accept-package-agreements"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, capture_output=True, text=True)
            if sshfail.returncode != 0:
                print("SSH not installed!")
                time.sleep(2)
            elif sshfail.returncode == 0:
                pass
        elif sshconfirm.lower() != y:
            clear()
            pass
        
elif keepgoing.lower() != y:
    clear()
    input("Okay! Stopping here! ")