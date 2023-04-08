# CatGen
i got tired of having to remember netcat commands so i made this script

start a netcat listener on a port or create a file (.bat most likely) that contains the command line arguments to connect to the netcat server

requires netcat to work, run 'pip3 install netcat' or 'pip3 install -r requirements.txt' inside CatGen directory after cloning  

instructions: edit 'catgen.py' and change 'ncport' number to any port of your choice and 'nchost' to the ip address of the host machine. optionally, you can change 'bandaid' from '-e cmd.exe' to '-e /bin/sh' if you want the script to make files containing commands for Unix Operating Systems instead of Windows.
