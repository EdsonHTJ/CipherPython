from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def en_AES(st,k):
    key = (bytes(k,'utf-8'))
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(bytes(st,'utf-8'))
    return ciphertext

def en_cesar(st,k):
    st_cesar = []
    for c in st:
        st_cesar.append(chr(ord(c)+int(k)%55291))
    return ''.join(st_cesar)

def dec_cesar(st,k):
    st_cesar = []
    for c in st:
        st_cesar.append(chr(ord(c)-int(k)%55291))
    return ''.join(st_cesar)

def en_xor(arr,k):
    bk=0
    chrkey=0
    for element in k:
        if element=='0':
            bk=bk*2
        elif element=='1':
            bk=bk*2+1
        else:
            chrkey=1
  #print("bk:"+bin(bk))
    if chrkey==0:
        xarr=[]
        for c in arr:
            hx=str(hex(ord(c)^bk))
            xarr.append(hx[2:])

        return ''.join(xarr)
    else:
        xarr=[]
        i=0
        for c in arr:
            hx=str(hex(ord(c)^ord(k[i%len(k)])))
            hnum=hx[2:]
            if(len(hnum)<2):
                hnum='0'+hnum
            xarr.append(hnum)
            i=i+1

        return ''.join(xarr)


def dec_xor(arr,k):
    bk=0
    for element in k:
        if element=='0':
            bk=bk*2
        elif element=='1':
            bk=bk*2+1
        else:
            chrkey=1
    #print("bk:"+bin(bk))
    if chrkey==0:
        xarr=[]
        for x in range(int(len(arr)/2)):
            hexs="0x"+arr[2*x]+arr[2*x+1]
            hexi=int(hexs, 16)
            xarr.append(chr(hexi^bk))
        return ''.join(xarr)
    else:
        xarr=[]
       # i=0
        for x in range(int(len(arr)/2)):
            hexs="0x"+arr[2*x]+arr[2*x+1]
            hexi=int(hexs, 16)
            xarr.append(chr(hexi^ord(k[x%len(k)])))
        return ''.join(xarr)

a= input('Palavra: ')
b= input('Chave: ')

print(en_AES(a,b))

