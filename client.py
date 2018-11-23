import sys
import TCP_Connection as tcp
import UDP_communication as udp

host_address = sys.argv[1]
host_port = sys.argv[2]
stcp = tcp.create_socket()
handshake = tcp.connection(host_address, host_port,stcp)
#Decoding (in a string) and printing the handshake message
print('Received handshake data from server:', handshake)
CID = handshake[6:15]
UDP_port = handshake[15:]
sudp = udp.create_socket()
udp.connection(host_address, UDP_port, sudp)
udp.send_message(CID,UDP_port,host_address, sudp)
udp.received_data(sudp)
tcp.close_socket(sudp)
tcp.close_socket(stcp)
