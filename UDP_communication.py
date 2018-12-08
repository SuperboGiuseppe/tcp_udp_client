import socket
import struct
import encryption



def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s

def send_message(CID, UDP_port, host_address, s, message, key):
    ack = True
    eom = False
    encrypted_message = encryption.encrypt_message(message, key)
    #print(message)
    data_remaining = 0
    #print(len(message))
    length = len(message)
    data = struct.pack('!8s??HH64s', bytes(CID, 'utf-8'), ack, eom, data_remaining, length, bytes(encrypted_message, 'utf-8'))
    s.sendto(data, (host_address, int(UDP_port)))


def received_data(s, key):
    print("Received data:")
    received_package = struct.unpack('!8s??HH64s', s.recv(1024))
    EOM = received_package[2]
    received_message = received_package[5]
    #print(received_message)
    #print(key)
    received_message = received_message.decode('UTF-8')
    received_message = received_message.rstrip('h\00')
    if EOM is not True:
        words = encryption.encrypt_message(received_message, key)
    else:
        words = received_message
    return words, EOM


def connection(host_address, UDP_port, s):
    # Encapsulating server informations (Address, port) inside a single array)
    server_address = (host_address, int(UDP_port))

    # Connection to the server with command line arguments
    s.connect(server_address)

def reverse_message(message):
    #print(message)
    list_words = message.split()
    #print(list_words)
    index = list_words[len(list_words)-1].find('\00')
    #print(index)
    if(index != -1):
        list_words[len(list_words)-1] = list_words[len(list_words)-1][0:index]
    #print(list_words)
    reversed_list = []
    for word in reversed(list_words):
        reversed_list.append(word)
    #print(reversed_list)
    return " ".join(reversed_list)
