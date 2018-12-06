import socket
import struct
import binascii


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s

def send_message(CID, UDP_port, host_address, s, message):
	ack = True
	eom = False
	#print(message)
	data_remaining = 0
	#print(len(message))
	length = len(message)
	data = struct.pack('!8s??HH64s', bytes(CID, 'utf-8'), ack, eom, data_remaining, length, bytes(message, 'utf-8'))
	s.sendto(data, (host_address, int(UDP_port)))


def received_data(s):
    print("Received data:")
    received_data = struct.unpack('!8s??HH64s', s.recv(2048))
    return received_data


def connection(host_address, UDP_port, s):
    # Encapsulating server informations (Address, port) inside a single array)
    server_address = (host_address, int(UDP_port))

    # Connection to the server with command line arguments
    s.connect(server_address)

def reverse_message(received_data):
	message = received_data.decode()
	#print(message)
	list_words = message[14:len(message)].split()
	#print(list_words)
	index = list_words[len(list_words)-1].find('\00')
	#print(index)
	if(index != -1):
		list_words[len(list_words)-1] = list_words[len(list_words)-1][0:index]
	print(list_words)
	reversed_list = []
	for word in reversed(list_words):
		reversed_list.append(word)
	print(reversed_list)
	return " ".join(reversed_list)