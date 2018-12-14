import random

def randomKey():

    key = ""
    char = "123456789ABCDEFabcdef"

    for i in range(64):

        subKey = char[random.randrange(16)]
        key += subKey
    
    return key

    '''
    Create a random key for encryption
    :return a 64 byte strings of hexadecimal characters
    '''

def createKeys():

    keys = ""
    subkey = ""

    for i in range(20):

        subkey = randomKey()
        keys += subkey + "\r\n"

    keys += ".\r\n"

    return keys

    '''
    Create a string with the 20 'client' keys for encryption with the format one key per line and the dot at the end
    :return a string of 20 'client' keys for encryption to send to the server
    '''

def splitKeys(keys):

    keyArray = keys.split("\r\n")
    del keyArray[-1]

    if keyArray[-1] is '.':

        del keyArray[-1]

        #for i in range(len(keyArray)):
            
            #keyArray[i] = keyArray[i].decode("utf-8")

        return keyArray

        '''
        Split the keys received from the server into and array
        :param keys: the string received from the server
        :return an array of the 20 'server' keys
        '''
        
def encrypt_message(message, key):

    cyphertext = ""
    for i in range(len(message)):
        # ord() return the ascii value, chr() the character related to the ascii value
        cyphertext += chr(ord(message[i]) ^ ord(key[i]))
    return cyphertext

    '''
    Can encrypt or decrypt a 64 byte strings text
    :param message: the message to encrypt or decrypt
    :param key: the key to use to encrypt or decrypt
    '''