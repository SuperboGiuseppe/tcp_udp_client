import socket

def connection(host_address, host_port):
	s = socket.socket()
	server_address=(host_address,int(host_port))
	s.connect(server_address)
	message = "HELLO\r\n"
	s.sendall(message.encode())
	handshake = s.recv(1024)
	s.close()
	print('Received data from server:', handshake.decode())

