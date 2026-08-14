import getpass, os, platform, shutil, sys, time, subprocess, urllib.request

def clear():
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

keepgoing = input("Continue? (y/n) ")
if keepgoing.lower() == "y":
    if shutil.which("winget"):
        pingcheck_win = subprocess.run(["ping", "-n", "1", "google.com"], capture_output=True, text=True)
        if pingcheck_win.returncode != 0:
            print("You don't actually have internet!")
            time.sleep(2)
            sys.exit(1)
        elif pingcheck_win.returncode == 0:
            print("You have internet!")
            time.sleep(1)

        # GIT

        gitconfirm = input("Install Git? (y/n) ")
        if gitconfirm.lower() == "y":
            print("\nInstalling Git!")
            git_fail = subprocess.run(["winget", "install", "Git.Git", "--silent", "--accept-source-agreements", "--accept-package-agreements"], capture_output=True, text=True)
            if git_fail.returncode != 0:
                print("Git installation failed!")
                time.sleep(2)
            elif git_fail.returncode == 0:
                pass
        elif gitconfirm.lower() != "y":
            clear()

        # ADB & FASTBOOT

        afconfirm = input("Install ADB & Fastboot? (y/n) ")
        if afconfirm.lower() == "y":
            print("Installing ADB & Fastboot!")
            af_fail = subprocess.run(["winget", "install", "Google.PlatformTools", "--silent", "--accept-source-agreements", "--accept-package-agreements"], capture_output=True, text=True)
            if af_fail.returncode != 0:
                print("ADB & Fastboot not installed!")
                time.sleep(2)
            elif af_fail.returncode == 0:
                pass
        elif afconfirm.lower() != "y":
            clear()

        # VISUAL STUDIO CODE (VSCODE)

        vsconfirm = input("Install Visual Studio Code? (y/n) ")
        if vsconfirm.lower() == "y":
            print("Installing VSCode!")
            vsfail = subprocess.run(["winget", "install", "Microsoft.VisualStudioCode", "--silent", "--accept-source-agreements", "--accept-package-agreements"], capture_output=True, text=True)
            if vsfail.returncode != 0:
                print("VSCode not installed!")
                time.sleep(2)
            elif vsfail.returncode == 0:
                pass
        elif vsconfirm.lower() != "y":
            clear()

        # SSH

        sshconfirm = input("Install SSH? (y/n) ")
        if sshconfirm.lower() == "y":
            print("Installing SSH!")
            sshfail = subprocess.run(["winget", "install", "Microsoft.OpenSSH.Beta", "--silent", "--accept-source-agreements", "--accept-package-agreements"], capture_output=True, text=True)
            if sshfail.returncode != 0:
                print("SSH not installed!")
                time.sleep(2)
            elif sshfail.returncode == 0:
                pass
        elif sshconfirm.lower() != "y":
            clear()

    elif platform.system() == "Linux":
        if shutil.which("pacman"):
            pingcheck_arch = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True)
            if pingcheck_arch.returncode != 0:
                print("You don't actually have internet!")
                time.sleep(2)
                sys.exit(1)
            elif pingcheck_arch.returncode == 0:
                print("You have internet!")
                time.sleep(1)

            # GIT
            
            pacgitconfirm = input("Install Git? (y/n) ")
            if pacgitconfirm.lower() == "y":
                print("Installing Git!")
                gitin = subprocess.run(["sudo", "pacman", "-Sy", "git", "--needed", "--noconfirm"], capture_output=True, text=True)
                if gitin.returncode != 0:
                    print("Failed to install git!")
                    time.sleep(2)
                elif gitin.returncode == 0:
                    pass
            elif pacgitconfirm.lower() != "y":
                clear()

            # ADB & FASTBOOT

            adbconfirm = input("Install ADB & Fastboot? (y/n) ")
            if adbconfirm.lower() == "y":
                print("Installing ADB & Fastboot!")
                adbin = subprocess.run(["sudo", "pacman", "-Sy", "android-tools", "--needed", "--noconfirm"], capture_output=True, text=True)
            elif adbconfirm.lower() != "y":
                clear()

            # VISUAL STUDIO CODE (VSCODE)

            vscodepac = input("Install Visual Studio Code (VSCode)? (y/n) ")
            if vscodepac.lower() == "y":
                parucheck = shutil.which("paru")
                yaycheck = shutil.which("yay")
                if parucheck:
                    parufail = subprocess.run(["paru", "-S", "visual-studio-code-bin", "--noconfirm"], capture_output=True, text=True)
                    if parufail.returncode != 0:
                        print("Failed to install VSCode!")
                        time.sleep(2)
                    elif parufail.returncode == 0:
                        pass
                elif yaycheck:
                    yayfail = subprocess.run(["yay", "-S", "visual-studio-code-bin", "--noconfirm"], capture_output=True, text=True)
                    if yayfail.returncode != 0:
                        print("Failed to install VSCode!")
                        time.sleep(2)
                    elif yayfail.returncode == 0:
                        pass
                else:
                    print("Installing an AUR helper!")
                    if not shutil.which("git"):
                        subprocess.run(["sudo", "pacman", "-S", "git", "--noconfirm"])
                    yayinstall = subprocess.run(["git", "clone", "https://aur.archlinux.org/yay.git", "&&", "cd", "yay"], capture_output=True, text=True)
                    if yayinstall.returncode != 0:
                        print("Failed to fetch yay AUR helper!")
                    elif yayinstall.returncode == 0:
                        print("Building yay AUR helper!")
                        if not shutil.which("fakeroot"):
                            subprocess.run(["sudo", "pacman", "-S", "base-devel", "--noconfirm"], capture_output=True, text=True)
                            subprocess.run(["makepkg","-si", "--noconfirm"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        else:
                            subprocess.run(["makepkg","-si", "--noconfirm"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        yayVSCode = subprocess.run(["yay", "-S", "visual-studio-code-bin", "--noconfirm"], capture_output=True, text=True)
                        if yayVSCode.returncode != 0:
                            print("Failed to install VSCode!")
                        elif yayVSCode.returncode == 0:
                            pass
            elif vscodepac.lower() != "y":
                clear()

            # SSH

            sshpac = input("Install SSH? (y/n) ")
            if sshpac.lower() != "y":
                clear()
            elif sshpac.lower() == "y":
                sshin = subprocess.run(["sudo", "pacman", "-S", "openssh", "--noconfirm"], capture_output=True, text=True)
                if sshin.returncode == 0:
                    pass
                else:
                    print("SSH failed to install!")
                if shutil.which("systemctl"):
                    subprocess.run(["sudo", "systemctl", "enable", "--now", "sshd"])
                elif shutil.which ("runit"):
                    subprocess.run(["sudo", "ln", "-s", "/etc/runit/sv/ssh", "/run/runit/sshd"])
                    subprocess.run(["sudo", "sv", "up", "sshd"])
                elif shutil.which ("dinitctl"):
                    subprocess.run(["sudo", "ln", "-s", "/etc/dinit.d/sshd", "/etc/dinit.d/boot.d/"])
                elif shutil.which("rc-update"):
                    subprocess.run(["sudo", "rc-update", "add", "sshd", "default"])
                    subprocess.run(["sudo", "rc-service", "sshd", "start"])
                elif shutil.which("s6-rc"):
                    subprocess.run(["sudo", "touch", "/etc/s6-rc/sv/sshd/run"])
                    subprocess.run(["sudo", "echo", "'#!/usr/bin/execlineb -P'", ">", "/etc/s6-rc/sv/sshd/run"])
                    subprocess.run(["sudo", "echo", "'fdmove -c 2 1'", ">>", "/etc/s6-rc/sv/sshd/run"])
                    subprocess.run(["sudo", "echo", "'exec /usr/bin/ssh'", ">>", "/etc/s6-rc/sv/sshd/run"])

            # DEBIAN/UBUNTU GIT     
                   
        elif shutil.which("apt"):
            pingcheck_deb = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True)
            if pingcheck_deb.returncode != 0:
                print("You don't actually have internet!")
                time.sleep(2)
                sys.exit(1)
            elif pingcheck_deb.returncode == 0:
                print("You have internet!")
                time.sleep(1)

            deb_git = input("Install Git? (y/n) ")
            if deb_git.lower() != "y":
                clear()
            elif deb_git.lower() == "y":
                print("Installing Git!")
                gitin_deb = subprocess.run(["sudo", "apt", "install", "git", "-y"], capture_output=True, text=True)
                if gitin_deb.returncode != 0:
                    print("Git failed to install!")
                elif gitin_deb.returncode == 0:
                    print("Git installed!")

            # ADB & FASTBOOT

            adb_deb = input("Install ADB & Fastboot? (y/n) ")
            if adb_deb.lower() != "y":
                clear()
            elif deb_git.lower() == "y":
                print("Installing ADB & Fastboot!")
                af_fail = subprocess.run(["sudo", "apt", "install", "adb", "fastboot", "-y"], capture_output=True, text=True)
                if af_fail.returncode != 0:
                    print("ADB & Fastboot failed to install!")
                elif af_fail.returncode == 0:
                    print("ADB & Fastboot installed!")

            # Nala APT

            if shutil.which("nala"):
                pass
            else:
                nala_in = input("Install Nala? It is a frontend for APT that is faster and prettier. (y/n) ")
                if nala_in.lower() != "y":
                    clear()
                elif nala_in.lower() == "y":
                    print("Installing Nala!")
                    nala_fail = subprocess.run(["sudo", "apt", "install", "nala", "-y"], capture_output=True, text=True)
                    if nala_fail.returncode != 0:
                        print("Nala failed to install!")
                    elif nala_fail.returncode == 0:
                        print("Nala installed!")

            # VSCode
            
            vs_deb = input("Install Visual Studio Code? (VSCode) (y/n) ")
            if vs_deb.lower() != "y":
                clear()
            else:
                url = "https://go.microsoft.com/fwlink/?LinkID=760868"
                file = "VSCode.deb"
                print("Grabbing VSCode app file from web!")
                urllib.request.urlretrieve(url, file)
                if os.path.isfile("VSCode.deb"):
                    input("The file is here on your computer now, but this script can't install it due to the file bringing up extra prompts. You'll have to install it later. Please click any key to continue! ")
                else:
                    print("Failed to grab VSCode installation package!")

            # SSH

            ssh_deb = input("Install SSH? (y/n) ")
            if ssh_deb.lower() != "y":
                clear()
            else:
                print("Installing SSH!")
                ssh_fail_deb = subprocess.run(["sudo", "apt", "install", "openssh-server", "-y"], capture_output=True, text=True)
                if ssh_fail_deb.returncode != 0:
                    print("Failed to install SSH!")
                else:
                    if shutil.which("systemctl"):
                        subprocess.run(["sudo", "systemctl", "enable", "--now", "sshd"])
                    else:
                        pass
            
elif keepgoing.lower() != "y":
    clear()
    input("Okay! Stopping here! ")