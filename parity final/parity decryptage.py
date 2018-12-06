def bin2dec(binary='0'):
    decimal = 0
    place = 1
    for i in range(len(binary)-1,-1,-1):
        decimal = decimal + int(binary[i])*place
        place=place*2   
    return (decimal) 

def paritybin(b="0"):
    par=b[-1]
    return par

def getParity( n ): 
    parity = 1
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    if (parity==1):
            parity="0"
    else:
            parity="1"
    return parity 

def suppar(c="0"):
    s=""
    for i in range(0,len(c)-1):
       s=s+c[i]
    return s

def split(l):
    k=0
    h=[]
    for j in range(0,len(l),8):
        s=""
        for i in range(0,8+k):
            s=s+l[j+i]
        h.append(s)
    return h

def transAndVerif(s):
    p1=split(s)
    g=0
    bin=0
    par=0
    finalstring=""
    for i in range(0,len(p1)):
        g=paritybin(p1[i])
        bin=bin2dec(suppar(p1[i]))
        par=getParity(bin)
        if g==par:
            finalstring=finalstring+chr(bin)
        else:
            print("error in the data")
            return 0
    return finalstring


    
         
    
l="1011011010101111001100110110101100101010"
c="11101"
print(suppar(c))
print(split(l))


