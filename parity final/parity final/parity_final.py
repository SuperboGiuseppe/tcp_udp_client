def getParity( n ): 
    parity = 1
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    return parity 
  
 
n = 7


def charac(s):

    k = []

    for i in range(0,len(s)):
        k.append(ord(s[i]))
    return k
    


def dec2bin(d,nb=0):
    if d==0:
        b="0"
    else:
        if (getParity(d)==1):
            b="0"
        else:
            b="1"
        while d!=0:
            b="01"[d&1]+b
            d=d>>1
    while len(b)<8:
        b="0"+b
    return b.zfill(nb)

def transf(d):
   s=""
   for i in range(0,len(d)):
       s=s+dec2bin(d[i])
   return s

c = "cocksucker"

print (dec2bin(4))
bita = dec2bin(6)
print (bita)
print (bita[-1])
j=charac(c)
print(j)
l=transf(j)
print(l)
