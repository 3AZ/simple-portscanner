import socket
import os
from colorama import Fore
from time import sleep

openprts = []
os.system("clear")
ip = input(Fore.BLUE + "Target IP: " + Fore.CYAN)
prt = int(input(Fore.BLUE + "Start Of Port Range: " + Fore.CYAN))
prt1 = int(input(Fore.BLUE + "End Of Port Range: " + Fore.CYAN))
while prt <= prt1:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.04)
		s.connect((ip, prt))
		s.close()
		print(Fore.GREEN + f"{str(prt)} OPEN")
		openprts.insert(0, prt)
		prt = prt + 1
	except:
		s.close()
		prt = prt + 1
		print(Fore.RED + f"{str(prt)} CLOSED")
print(Fore.CYAN + "Open Ports:")
print(Fore.GREEN)
for p in openprts:
	print(p)