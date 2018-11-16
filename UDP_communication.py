import socket
import struct

def send_message(CID, UDP_port, host_address, host_port,s):
	message = 'Hello from '
	message+=CID
	ack = True
	eom = False
	data_remaining = 0
	length = len(message)
	#data = struct.pack('!??H', CID, ack, eom)
	data = struct.pack(data_remaining, length, message)
	s.sendto(data, (host_address, UDP_port))

def received_data(s):
	print("Received data:")
	received_data = s.recv(1024)
	print(received_data)
	
