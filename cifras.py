from Crypto.Cipher import AES,DES3
from Crypto import Random

nonce = 0
iv = Random.new().read(DES3.block_size)
def en_DES(st,k):
    #try:
        key = bytes(k,'utf-8')
        #key = b'Sixteen byte key'
        cipher = DES3.new(key, DES3.MODE_CBC,iv)
        ciphertext = cipher.encrypt(bytes(st,'utf-8'))
        Ct=[]
        for element in ciphertext:
            hx = str(hex(element))
            hnum = hx[2:]
            if(len(hnum)<2):
                    hnum='0'+hnum
            Ct.append(hnum)
        return ''.join(Ct)
    #except:
        return 'Chave Invalida'

def dec_DES(st,k):
    #try:
        toDec=[]
        for x in range(int(len(st)/2)):
            hexs="0x"+st[2*x]+st[2*x+1]
            hexi=int(hexs, 16)
            toDec.append(hexi)
        key = bytes(k,'utf-8')
        #key = b'Sixteen byte key'
        cipher = DES3.new(key, DES3.MODE_CBC,iv)
        plaintext = cipher.decrypt(bytes(toDec))
        return (str(plaintext))[2:len(str(plaintext))-1]
        #return(plaintext)
    #except:
        return 'Chave Invalida'




def en_AES(st,k):
    global nonce
    key = (bytes(k,'utf-8'))
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(bytes(st,'utf-8'))
    Ct=[]
    #print(ciphertext)
    for element in ciphertext:
        hx = str(hex(element))
        hnum = hx[2:]
        if(len(hnum)<2):
                hnum='0'+hnum
        Ct.append(hnum)

        
    return ''.join(Ct)

def dec_AES(st,k):
    toDec=[]
    for x in range(int(len(st)/2)):
        hexs="0x"+st[2*x]+st[2*x+1]
        hexi=int(hexs, 16)
        toDec.append(hexi)
    key = (bytes(k,'utf-8'))
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(bytes(toDec))
    return (str(plaintext))[2:len(str(plaintext))-1]
    

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

a=input('Palavra: ')
b="aaaavvvvccccdddd"

a = en_DES(a,b)
print(a)
a = dec_DES(a,b)
print(a)
