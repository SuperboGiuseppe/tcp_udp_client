import socket

def connection(host_address, host_port):
    s = socket.socket()
    s.connect(host_address,host_port)
    s.sendall('HELLO\r\n')
    handshake = s.recv(1024)
    s.close()
    print('Received data from server:', handshake)

