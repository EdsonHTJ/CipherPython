from Crypto.Cipher import AES,DES3
from Crypto import Random
import sDES

def en_sDES(st,k,mode=0):
    Ct=[]
    if mode ==0:
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
    else:
        for element in st:
            arrb = str(bin(element))[2:]
            while len(arrb)<8:
                arrb= '0'+arrb
            Ct.append(int(sDES.enc_sDES_8b(arrb,k),2))
        return Ct


def dec_sDES(st,k,mode=0):
    Pt=[]
    if mode==0:
        for x in range(int(len(st)/2)):
            hexs="0x"+st[2*x]+st[2*x+1]
            bini=str(bin(int(hexs, 16)))[2:]
            while len(bini)<8:
                bini = '0'+bini
            Pt.append(chr(int('0b'+sDES.dec_sDES_8b(bini,k),2)))
        return ''.join(Pt)
    else:
        for element in st:
            arrb = str(bin(element))[2:]
            while len(arrb)<8:
                arrb= '0'+arrb
            Pt.append(int(sDES.dec_sDES_8b(arrb,k),2))
        return Pt

def en_DES(st,k,mode=0):
    key = bytes(k,'utf-8')
    #key = b'Sixteen byte key'
    iv = Random.new().read(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_OFB,iv)
    if mode==0:
        ciphertext = iv+cipher.encrypt(bytes(st,'utf-8'))
        Ct=[]
        for element in ciphertext:
            hx = str(hex(element))
            hnum = hx[2:]
            if(len(hnum)<2):
                    hnum='0'+hnum
            Ct.append(hnum)
        return ''.join(Ct)
    else:
        ciphertext = iv+cipher.encrypt(st)
        return ciphertext

def dec_DES(st,k,mode=0):
    key = bytes(k,'utf-8')
    if mode == 0:
        toDec=[]
        for x in range(int(len(st)/2)):
            hexs="0x"+st[2*x]+st[2*x+1]
            hexi=int(hexs, 16)
            toDec.append(hexi)
        iv = bytes(toDec[0:8])
        msg = toDec[8:]
        cipher = DES3.new(key, DES3.MODE_OFB,iv)
        plaintext = cipher.decrypt(bytes(msg))
        return (str(plaintext))[2:len(str(plaintext))-1]
    else:
        iv = st[0:8]
        msg = st[8:]
        cipher = DES3.new(key, DES3.MODE_OFB,iv)
        plaintext = cipher.decrypt(msg)
        return plaintext



def en_AES(st,k,mode=0):

    key = (bytes(k,'utf-8'))
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    if mode == 0:
        ciphertext, tag = cipher.encrypt_and_digest(bytes(st,'utf-8'))
        ciphertext = nonce + ciphertext
        Ct=[]
        for element in ciphertext:
            hx = str(hex(element))
            hnum = hx[2:]
            if(len(hnum)<2):
                    hnum='0'+hnum
            Ct.append(hnum)
        return ''.join(Ct)
    else:
        ciphertext, tag = cipher.encrypt_and_digest(st)
        ciphertext = nonce + ciphertext
        return ciphertext


def dec_AES(st,k,mode=0):
    key = (bytes(k,'utf-8'))
    if mode == 0:
        toDec=[]
        for x in range(int(len(st)/2)):
            hexs="0x"+st[2*x]+st[2*x+1]
            hexi=int(hexs, 16)
            toDec.append(hexi)
        nonce = toDec[:16]
        msg = toDec[16:]
        cipher = AES.new(key, AES.MODE_EAX, nonce=bytes(nonce))
        plaintext = cipher.decrypt(bytes(msg))
        return (str(plaintext))[2:len(str(plaintext))-1]
    else:
        nonce = st[:16]
        msg = st[16:]
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt(msg)
        return plaintext


def en_cesar(st,k,mode=0):
    st_cesar = []
    if mode==0:
        for c in st:
            st_cesar.append(chr(((ord(c)+int(k)))%256))
        return ''.join(st_cesar)
    else:
        for element in st:
            st_cesar.append((element+int(k))%256)
        return st_cesar



def dec_cesar(st,k,mode=0):
    st_cesar = []
    if mode==0:
        for c in st:
            st_cesar.append(chr(ord(c)-int(k)%256))
        return ''.join(st_cesar)
    else:
        for element in st:
            st_cesar.append((element-int(k))%256)
        return st_cesar

def en_xor(arr,k,mode=0):
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
        if mode == 0:
            for c in arr:
                hx=str(hex(ord(c)^bk))
                xarr.append(hx[2:])
            return ''.join(xarr)
        else:
            for c in arr:
                hx=(c^bk)
                xarr.append(hx)
            return xarr

    else:
        xarr=[]
        i=0
        if mode == 0:
            for c in arr:
                hx=str(hex(ord(c)^ord(k[i%len(k)])))
                hnum=hx[2:]
                if(len(hnum)<2):
                    hnum='0'+hnum
                xarr.append(hnum)
                i=i+1
            return ''.join(xarr)
        else:
            for c in arr:
                hx=c^ord(k[i%len(k)])
                xarr.append(hx)
                i=i+1
            return xarr


def dec_xor(arr,k,mode=0):
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
        if mode ==0:
            for x in range(int(len(arr)/2)):
                hexs="0x"+arr[2*x]+arr[2*x+1]
                hexi=int(hexs, 16)
                xarr.append(chr(hexi^bk))
            return ''.join(xarr)
        else:
            for x in range(len(arr)):
                xarr.append(arr[x]^bk)
            return xarr

    else:
        xarr=[]
        if mode == 0:
            for x in range(int(len(arr)/2)):
                hexs="0x"+arr[2*x]+arr[2*x+1]
                hexi=int(hexs, 16)
                xarr.append(chr(hexi^ord(k[x%len(k)])))
            return ''.join(xarr)
        else:
            for x in range(len(arr)):
                xarr.append((arr[x]^ord(k[x%len(k)])))
            return xarr



#f = open('teste.png','rb').read()

#fcp = en_xor(f,'aabaa',1)

#open('testecrit.png','wb').write(bytes(fcp))
#f = open('testecrit.png','rb').read()

#fcp = dec_xor(f,'aabaa',1)

#open('testedescrit.png','wb').write(bytes(fcp))




