import socket

def connection(host_address, host_port):
	#Creation of client socket
	s = socket.socket()
	
	#Encapsulating server informations (Address, port) inside a single array)
	server_address=(host_address,int(host_port))

	#Connection to the server with command line arguments
	s.connect(server_address)

	#Encapsulating message in a variable, required as we need to use encode function to send 		#our message in bytes  
	message = "HELLO\r\n"

	#Sending the message to the server
	s.sendall(message.encode())
	
	#Receiving the server answer in handshake variable
	handshake = s.recv(1024)

	#Closing the socket, to be removed as we need to establish a UDP communication after the 		#handshake
	s.close()
	
	#Decoding (in a string) and printing the handshake message
	print('Received data from server:', handshake.decode())

