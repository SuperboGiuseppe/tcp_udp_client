import socket
import struct

def create_socket():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return s

def send_message(CID, UDP_port, host_address, s):
	message = "Hello from "
	message+=CID
	print(message)
	ack = True
	eom = False
	data_remaining = 0
	length = len(message)
	print(int(UDP_port))
	data = struct.pack('!s??iis', bytes(CID, 'utf-8'), ack, eom, data_remaining, length, bytes(message, 'utf-8'))
	s.sendto(data, (host_address, int(UDP_port)))

def received_data(s):
	print("Received data:")
	while True:
		received_data = s.recv(1024)
		print(received_data)
	
def connection(host_address, UDP_port, s):

	#Encapsulating server informations (Address, port) inside a single array)
	server_address=(host_address,int(UDP_port))

	#Connection to the server with command line arguments
	s.connect(server_address)
