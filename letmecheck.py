import socket
from termcolor import colored

def scan(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		serviceVersion = sock.recv(1024)
		serviceVersion = serviceVersion.decode('utf-8')
		serviceVersion = serviceVersion.strip('\n')
		portstate = f'Port {str(port)} is open'
		print(colored(portstate,'green'), end='  ')
		print(serviceVersion)
	except ConnectionRefusedError:
		print(colored(f'Port {str(port)} is closed','red'))
	except UnicodeDecodeError:
		print(colored(f'Port {str(port)} is open','green'))

target = input('Target: ')
ports = input('Ports: ')

if ',' in ports:
	portlist = ports.split(',')
	for port in portlist:
		scan(target, int(port))
elif '-' in ports:
	portrange = ports.split('-')
	start = int(portrange[0])
	end = int(portrange[1])
	for port in range(start, end+1):
		scan(target, port)
else:
	scan(target, int(ports))