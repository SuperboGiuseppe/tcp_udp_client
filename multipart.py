import UDP_communication as udp

def receive_parts(s, key, key_index):
    data_remaining = -1
    message = ''
    k=key_index
    while(data_remaining != 0):
        if(k == 0):
            #print(key[k][0:65])
            words, EOM, data_remaining = udp.received_data(s, key[k][1:65])
        else:
            #print(key[k][0:65])
            words, EOM, data_remaining = udp.received_data(s, key[k][0:65])
        #print(data_remaining)
        message += words
        #print(message)
        k += 1
    print("Received message:", message)
    return message, EOM, k

def send_parts(CID, UDP_port, host_address, s, message, key, key_index):
    print("Reversed message:", message)
    length = len(message)
    data_remaining = length
    i = 0
    k = key_index
    while(data_remaining != 0):
        if(data_remaining <= 64):
            piece = message[i:i+data_remaining+1]
            data_remaining = 0
            print(piece)
            print("Length of piece:" , len(piece))
            print("KEY:", key[k][0:64])
            print("Length of key:", len(key[k][0:64]))
            udp.send_message(CID, UDP_port, host_address, s, piece, key[k][0:64], data_remaining)
        if(data_remaining > 64 and i == 0):
            piece = message[i:i+64]
            data_remaining -= 64
            print(piece)
            print("Length of piece:" , len(piece))
            print("KEY:", key[k][0:64])
            print("Data left:", data_remaining)
            print("Length of key:", len(key[k][0:64]))
            udp.send_message(CID, UDP_port, host_address, s, piece, key[k][0:64], data_remaining)
        if (data_remaining > 64 and i != 0):
            piece = message[i:i + 63]
            data_remaining -= 64
            print(piece)
            print("Length of piece:" , len(piece))
            print("Data left:", data_remaining)
            print("KEY:", key[k][0:64])
            print("Length of key:", len(key[k][0:64]))
            udp.send_message(CID, UDP_port, host_address, s, piece, key[k][0:64], data_remaining)
        i += 64
        k += 1
    return k