import sys
import TCP_Connection as tcp
import UDP_communication as udp

host_address = sys.argv[1]
host_port = sys.argv[2]
s = tcp.create_socket()
handshake = tcp.connection(host_address, host_port,s)
#Decoding (in a string) and printing the handshake message
print('Received handshake data from server:', handshake)
CID = handshake[6:15]
UDP_port = handshake[15:]
udp.send_message(CID,UDP_port,host_address,host_port,s)
udp.recevied_data(s)
tcp.close_socket(s)
