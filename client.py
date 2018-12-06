import sys
import TCP_Connection as tcp
import UDP_communication as udp
import encryption
import binascii

def main():
    host_address = sys.argv[1]
    host_port = sys.argv[2]
    socket_tcp = tcp.create_socket()
    keys = encryption.createKeys()
    handshake = tcp.connection(host_address, host_port, socket_tcp, keys)
    keys = encryption.splitKeys(keys)
    # Decoding (in a string) and printing the handshake message
    print('Received handshake data from server:', handshake)
    tcp.close_socket(socket_tcp)
    CID = handshake[6:15]
    UDP_port = handshake[15:20]
    array_key = encryption.splitKeys(handshake[21:])
    socket_udp = udp.create_socket()
    udp.connection(host_address, UDP_port, socket_udp)
    message = "Hello from "
    message += CID
    encrypted_message = encryption.encrypt_message(message, keys[1])
    print("Sent message:", encrypted_message)
    udp.send_message(CID, UDP_port, host_address, socket_udp, encrypted_message)
    received_package = udp.received_data(socket_udp)
    received_message = received_package[5]
    print("Test:",received_message)
    received_message = received_message.decode('UTF-8')
    print("Test:", received_message)
    received_message = received_message.rstrip('h\x00')
    print("Test:", received_message)
    print(array_key[1])
    test = encryption.encrypt_message(received_message, array_key[1])
    print(test)
    """
    test = udp.reverse_message(udp.received_data(socket_udp))
    print(test)
    udp.send_message(CID, UDP_port, host_address, socket_udp, test)
    print(udp.received_data(socket_udp))
    """
    tcp.close_socket(socket_udp)
    tcp.close_socket(socket_tcp)

if __name__ == '__main__':
    main()
