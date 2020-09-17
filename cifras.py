from Crypto.Cipher import AES,DES3
from Crypto import Random
import sDES

nonce = 0

def en_sDES(st,k):
    Ct=[]
    Bst = bytes(st,'utf-8')
    for element in Bst:
        arr = str(bin(element))[2:]
        while len(arr)<8:
            arr= '0'+arr
        hnum = str(hex(int('0b'+sDES.enc_sDES_8b(arr,k),2)))[2:]
        if(len(hnum)<2):
            hnum='0'+hnum
        Ct.append(hnum)
    return ''.join(Ct)
def dec_sDES(st,k):
    Pt=[]
    for x in range(int(len(st)/2)):
        hexs="0x"+st[2*x]+st[2*x+1]
        bini=str(bin(int(hexs, 16)))[2:]
        while len(bini)<8:
            bini = '0'+bini
        Pt.append(chr(int('0b'+sDES.dec_sDES_8b(bini,k),2)))
    return ''.join(Pt)
def en_DES(st,k):
    key = bytes(k,'utf-8')
    #key = b'Sixteen byte key'
    iv = Random.new().read(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_OFB,iv)
    ciphertext = iv+cipher.encrypt(bytes(st,'utf-8'))
    Ct=[]
    for element in ciphertext:
        hx = str(hex(element))
        hnum = hx[2:]
        if(len(hnum)<2):
                hnum='0'+hnum
        Ct.append(hnum)
    return ''.join(Ct)
def dec_DES(st,k):
    toDec=[]
    for x in range(int(len(st)/2)):
        hexs="0x"+st[2*x]+st[2*x+1]
        hexi=int(hexs, 16)
        toDec.append(hexi)
    key = bytes(k,'utf-8')
    iv = bytes(toDec[0:8])
    msg = toDec[8:]
    cipher = DES3.new(key, DES3.MODE_OFB,iv)
    plaintext = cipher.decrypt(bytes(msg))
    return (str(plaintext))[2:len(str(plaintext))-1]
def en_AES(st,k):
    global nonce
    key = (bytes(k,'utf-8'))
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(bytes(st,'utf-8'))
    Ct=[]
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
    if chrkey==0:
        xarr=[]
        for x in range(int(len(arr)/2)):
            hexs="0x"+arr[2*x]+arr[2*x+1]
            hexi=int(hexs, 16)
            xarr.append(chr(hexi^bk))
        return ''.join(xarr)
    else:
        xarr=[]
        for x in range(int(len(arr)/2)):
            hexs="0x"+arr[2*x]+arr[2*x+1]
            hexi=int(hexs, 16)
            xarr.append(chr(hexi^ord(k[x%len(k)])))
        return ''.join(xarr)
