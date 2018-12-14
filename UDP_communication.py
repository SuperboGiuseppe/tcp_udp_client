import socket
import struct
import encryption


def create_socket():
    '''
    Creating a new UDP socket to execute send/receive actions
    :return: Socket ready to be used by the caller module
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s


def send_message(CID, UDP_port, host_address, s, message, key, data_remaining):
    '''
    Sending a message to a specific UDP port by packing a complete UDP packet with all the necessary fields.
    :param CID: Client identification number to be recognized by the server whenever the client wants to send a message
    :param UDP_port: UDP port where the message is going to be directed
    :param host_address: Server address that is going to receive the message from the client
    :param s: Socket where the sending message occures
    :param message: Message to be sent to the server
    :param key: Specific key used to encode the message
    :param data_remaining: In multipart feature, this value tells how many bytes are left to be sent to the server
    '''
    ack = True
    eom = False
    encrypted_message = encryption.encrypt_message(message, key)
    length = len(message)
    data = struct.pack('!8s??HH64s', bytes(CID, 'utf-8'), ack, eom, data_remaining, length,bytes(encrypted_message, 'utf-8'))
    s.sendto(data, (host_address, int(UDP_port)))


def received_data(s, key):
    '''
    Receiving a message from the socket connected to the UDP port of the server
    :param s: Socket used for listening the server messages
    :param key: Key used to decode the message received from the server
    :return words: Part of the message received from the server
    :return EOM: Flag used by the server to close the communication client-server
    :return data_remaining: How many bytes remain to be received from the server
    '''
    #print("Received part:")
    received_package = struct.unpack('!8s??HH64s', s.recv(1024))
    EOM = received_package[2]
    data_remaining = received_package[3]
    received_message = received_package[5]
    #print(received_message)
    #print(key)
    received_message = received_message.decode('UTF-8')
    received_message = received_message.rstrip('h\00')
    if EOM is not True:
        words = encryption.encrypt_message(received_message, key)
        #print(words)
    else:
        words = received_message
    return words, EOM, data_remaining


def connection(host_address, UDP_port, s):
    '''
    Connecting an existent socket to a specific UDP port of a server
    :param host_address: IP address of the server
    :param UDP_port: UDP port where the socket is going to be connected
    :param s: Socket to be connected to the UDP port of the server
    '''
    # Encapsulating server informations (Address, port) inside a single array)
    server_address = (host_address, int(UDP_port))

    # Connection to the server with command line arguments
    s.connect(server_address)

def reverse_message(message):
    '''
    Function that reverse the order of the words of a message previously received from the server
    :param message: message to be reversed
    :return: Message reversed
    '''
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
