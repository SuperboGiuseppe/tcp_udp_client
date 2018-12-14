import socket

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s


def connection(host_address, host_port, s, keys):
    # Encapsulating server informations (Address, port) inside a single array)
    server_address = (host_address, int(host_port))
    # Connection to the server with command line arguments
    s.connect(server_address)
    # Encapsulating message in a variable, required as we need to use encode function to send 		#our message in bytes
    message = "HELLO ENC MUL\r\n" + keys
    # Sending the message to the server
    s.sendall(message.encode())
    # Receiving the server answer in handshake variable
    handshake = s.recv(2048)
    return handshake.decode()


def close_socket(s):
    # Closing the socket connection
    s.close()
