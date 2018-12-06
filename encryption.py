import random

def randomKey():

    key = ""
    char = "123456789ABCDEFabcdef"

    for i in range(64):

        subKey = char[random.randrange(16)]
        key += subKey
    
    return key

def createKeys():

    keys = ""
    subkey = ""

    for i in range(20):

        subkey = randomKey()
        keys += subkey + "\r\n"

    keys += ".\r\n"

    return keys

def splitKeys(keys):

    keyArray = keys.split("\r\n")
    del keyArray[-1]

    if keyArray[-1] is '.':

        del keyArray[-1]

        #for i in range(len(keyArray)):
            
            #keyArray[i] = keyArray[i].decode("utf-8")

        return keyArray
        
def encrypt_message(message, key):

    cyphertext = ""
    for i in range(len(message)):
        # ord() return the ascii value, chr() the character related to the ascii value
        cyphertext += chr(ord(message[i]) ^ ord(key[i]))
    return cyphertext