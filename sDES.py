
def fk(arr,k):
    Ip = arr
    IpH = Ip[:4]
    IpL = Ip[4:]
    #print(Ip)
    #print(IpH+IpL)

    EP = IpL[4-1]+IpL[1-1]+IpL[2-1]+IpL[3-1]+IpL[2-1]+IpL[3-1]+IpL[4-1]+IpL[1-1]
    #print(EP)
    xor=int('0b'+EP,2)^int('0b'+k,2)
    xor=str(bin(xor))
    xor=xor[2:]
    while len(xor)<8:
         xor='0'+xor
    #print(xor)
    xorH = xor[:4]
    xorL = xor[4:]
    s0 = [
        [1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2]
    ]
    
    s1 = [
        [0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]
    ]
    
    SS0 = s0[int('0b'+xorH[1-1]+xorH[4-1],2)][int('0b'+xorH[2-1]+xorH[3-1],2)]
    #print(SS0)
    SS1 = s1[int('0b'+xorL[1-1]+xorL[4-1],2)][int('0b'+xorL[2-1]+xorL[3-1],2)]
    #print(SS1)
    SS0 = str(bin(SS0))[2:]
    SS1 = str(bin(SS1))[2:] 
    while(len(SS0)<2):
        SS0 = '0'+SS0
    
    while(len(SS1)<2):
        SS1 = '0'+SS1

    SS = SS0 + SS1
    p4 = SS[2-1]+SS[4-1]+SS[3-1]+SS[1-1]
    
    xor2=int('0b'+p4,2)^int('0b'+IpH,2)
    xor2=str(bin(xor2))[2:]
    while len(xor2)<4:
         xor2='0'+xor2
    return(xor2+IpL)

def key_gen(k):
    p10= k[3-1]+k[5-1]+k[2-1]+k[7-1]+k[4-1]+k[10-1]+k[1-1]+k[9-1]+k[8-1]+k[6-1]
    Ls11 = p10[1:5]+p10[0]
    Ls12 = p10[6:]+p10[5]
    Ls1 = Ls11 + Ls12
    k1 = Ls1[6-1]+Ls1[3-1]+Ls1[7-1]+Ls1[4-1]+Ls1[8-1]+Ls1[5-1]+Ls1[10-1]+Ls1[9-1]
    Ls21 = Ls11[2:]+Ls11[:2]
    Ls22 = Ls12[2:]+Ls12[:2]
    Ls2 = Ls21+Ls22
    k2 = Ls2[6-1]+Ls2[3-1]+Ls2[7-1]+Ls2[4-1]+Ls2[8-1]+Ls2[5-1]+Ls2[10-1]+Ls2[9-1]
    return (k1,k2)

def enc_sDES_8b(arrb,k):

    k1,k2 = key_gen(k)

    Ip = arrb[2-1]+arrb[6-1]+arrb[3-1]+arrb[1-1]+arrb[4-1]+arrb[8-1]+arrb[5-1]+arrb[7-1]

    saida = fk(Ip,k1)
    sw = saida[4:]+saida[:4]
    saida2 = fk(sw,k2)

    cipherbyte = saida2[4-1]+saida2[1-1]+saida2[3-1]+saida2[5-1]+saida2[7-1]+saida2[2-1]+saida2[8-1]+saida2[6-1]
    return cipherbyte

def dec_sDES_8b(arrb,k):

    k1,k2 = key_gen(k)

    Ip = arrb[2-1]+arrb[6-1]+arrb[3-1]+arrb[1-1]+arrb[4-1]+arrb[8-1]+arrb[5-1]+arrb[7-1]

    saida = fk(Ip,k2)
    sw = saida[4:]+saida[:4]
    saida2 = fk(sw,k1)

    plainbyte = saida2[4-1]+saida2[1-1]+saida2[3-1]+saida2[5-1]+saida2[7-1]+saida2[2-1]+saida2[8-1]+saida2[6-1]
    return plainbyte



