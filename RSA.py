import random
import fractions
import math
import sys

def LCM(x,y):#最小公倍数
    return x * y // math.gcd(x,y)

def ExtendedEuclid(x,y):#拡張ユークリッドの互除法
    #if(x<0 or y<0):return 0
    
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1
 
    while c1 != 0:
        m = c0 % c1
        q = c0 // c1
 
        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
 
    return c0, a0, b0

def Congruence(a,m):#一次合同式 (ax≡1 mod m) を解く
    i,D,k = ExtendedEuclid(a,m)
    return D % m

def CheckEven(n):#偶数かどうかを判定。偶数だったらTrue
    if n & 1 == 0:
        return True
    else:
        return False

def CheckPrime(n):#素数かどうか判定。素数だったらTrue
    if n == 2: return True
    if n <= 1 or CheckEven(n):return False

    d = (n - 1) >> 1
    while CheckEven(n):
        d >>= 1

    for i in range(100):
        a = random.randint(1,n-1)
        t = d
        y = pow(a,t,n)

        while t != n -1 and y != 1 and y != n - 1:
            y = pow(y,2,n)
            t <<= 1
        
        if y != n - 1 and CheckEven(t):
            return False

    return True

def GetRandomPrime(max):#max未満のランダムな素数を返す。存在しない場合は-1を返す
    if(max <= 1):return -1
    
    while(True):
        rand = random.randint(2,max)
        if(CheckEven(rand)):rand += 1
        if(CheckPrime(rand)):break
    
    return rand





def GenerateKeys(p,q):#二つの素数から秘密鍵と公開鍵を生成
    N = p * q
    L = LCM(p-1,q-1)
    E = 0
    D = 0

    for i in range(2,L):
        if math.gcd(i,L)==1:
            E = i
            break
        
    D = Congruence(E,L)

    return (E,N),(D,N)

def Encryption(plainText,publicKey):#公開鍵で暗号化
    E,N=publicKey
    plainInteger = [ord(char) for char in plainText]
    encrytedInteger = [pow(i,E,N) for i in plainInteger]
    encrytedText = ([str(i) for i in encrytedInteger])

    return encrytedText

def Decryption(encryedText,privateKey):#秘密鍵で復号化
    D,N = privateKey
    encrytedInteger = [int(char) for char in encrytedText]
    decrytedInteger = [pow(i,D,N) for i in encrytedInteger]
    decrytedtext = ''.join([chr(char) for char in decrytedInteger])

    return decrytedtext




if __name__ == '__main__':

    digit = 100
    p = GetRandomPrime(10**digit)
    q = GetRandomPrime(10**digit)
    publicKey,privateKey = GenerateKeys(p,q)

    plainText = input("Please Text\n")
    if plainText=="":
        print("Error")
        sys.exit()

    encrytedText = Encryption(plainText,publicKey)
    decrytedText = Decryption(encrytedText,privateKey)

    print(f"PlainText:{plainText}\n")

    print(f"PrivateKey:{publicKey}\n")
    print(f"PrivateKey:{privateKey}\n")

    print(f"CipherText:{encrytedText}\n")
    print(f"DecryptedText:{decrytedText}\n")

