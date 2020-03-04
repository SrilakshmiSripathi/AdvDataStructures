import random
import FindNextPrime

def SecHash(key, N):
    return (((7 - key)) % N) + 1
def linear():
    return 1
##def Search():
def Hash():
    TabSize = 11
    Type = "Double"
    hashTab = [None] * TabSize
    p = [22,45,42,57,88,11,31,27,2]
    kk = 0
    while kk < len(p):
##        k = random.randint(25, 75)
##    for k in
        k = p[kk]
        idx = k % TabSize
        print ("k", k, "\t", idx)
        if hashTab[idx] is None:
            print("Found empty spot at", idx) 
            hashTab[idx] = k
            kk =  kk + 1
            print("hashTab", hashTab)
        elif Type is "Double":
            while hashTab[idx] != None:
                print("\t\t collision occured at", idx)
                print("\n hashTab", hashTab)
                x = SecHash(k, TabSize)
                print ("SecHash, pos, next index", idx, x)
                print("\n hashTab", hashTab)
##                print("hashTab[idx + x]", hashTab[idx + x])
##                if hashTab[x] == None:
##                    hashTab[x] = k
##                    kk = kk + 1
                
                for i in range(x):
                    if idx + i <= len(hashTab):
                        idx = idx + i
                    else:
                        idx = idx + i - len(hashTab)
                if hashTab[idx] == None:
##                                 hashTab[idx] = k
                kk = kk + 1
##                if idx + x > len(hashTab) and hashTab[idx] == None:
####                    print ("x - len(hashTab) ",x - len(hashTab) )
####                    idx = idx + x - len(hashTab)
####                    print("idx",idx)
##                    hashTab[(idx + x) % TabSize] = k
##                elif hashTab[idx] == None and idx + x < len(hashTab):
##                    idx = idx + x
##                    hashTab[idx] = k
##                else:
##                    idx = idx + x
##            if hashTab[idx] is None:
##                 hashTab[idx] = k
        
##    print("hashTab", hashTab)
Hash()

##        
##         
##main()
##n = 10
##    
##print(FindNextPrime.primes(n//2))

    

##elif Type is "Linear":
##            if pos < len(hashTab) and hashTab[pos] != None:
##                x = linear()
##                print ("linear", x)
##                pos = pos + x
##                hashTab[pos] = k
##            elif pos is len(hashTab):
##                pos = 0
##                pos = pos + x
##                hashTab[pos] = k    
    
