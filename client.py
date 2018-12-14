import sys
import TCP_Connection as tcp
import UDP_communication as udp
import encryption
import multipart as mul

def main():
    host_address = sys.argv[1]
    host_port = sys.argv[2]
    socket_tcp = tcp.create_socket()
    client_keys = encryption.createKeys()
    handshake = tcp.connection(host_address, host_port, socket_tcp, client_keys)
    client_keys = encryption.splitKeys(client_keys)
    # Decoding (in a string) and printing the handshake message
    print('Received handshake data from server:', handshake)
    print("------------------------")
    print("Client keys :", client_keys)
    #tcp.close_socket(socket_tcp)
    CID = handshake[6:15]
    UDP_port = handshake[15:20]
    server_keys = encryption.splitKeys(handshake[21:])
    socket_udp = udp.create_socket()
    udp.connection(host_address, UDP_port, socket_udp)
    message = "Hello from "
    message += CID
    udp.send_message(CID, UDP_port, host_address, socket_udp, message, client_keys[0], 0)
    key_index_server = 0
    key_index_client = 1
    received_words, EOM, key_index_server = mul.receive_parts(socket_udp, server_keys, key_index_server)
    #print(received_words)
    i=1
    while(EOM != True):
        key_index_client = mul.send_parts(CID, UDP_port, host_address, socket_udp, udp.reverse_message(received_words), client_keys, key_index_client)
        received_words, EOM, key_index_server = mul.receive_parts(socket_udp, server_keys, key_index_server)
        print(received_words)
        i += 1
    tcp.close_socket(socket_udp)
    tcp.close_socket(socket_tcp)

if __name__ == '__main__':
    main()
