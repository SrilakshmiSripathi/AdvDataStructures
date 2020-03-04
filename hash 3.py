import sys
import math
import random
import FindNextPrime


def FHash(key, N):
    return (19 * key + 5) % N


def SecHash(key, N):
    # Taking table size half of original table
    n = FindNextPrime.primes(N//2)
    return ((107 * key) - 37) % n + 1


def linear():
    return 1


def probes(htab, pos1, pos2):
    # Find position circularly if empty spot found return position
    if pos1 + pos2 <= len(htab) - 1:
        pos1 = pos1 + pos2
    else:
        pos1 = pos1 + pos2 - (len(htab) - 1) - 1

    if htab[pos1] == None:
        return pos1
    else:
        return probes(htab, pos1, pos2)


def probCnt(htab, ky, p1, p2, start, prbs=0, hits=0, miss=0):
    """ Find hit or miss and total number of probes to find it"""
    if htab[p1] != ky:
        # if key not found, find circularly for next index
        if p1 == start and prbs != 0:
            # Hit miss if one cycle couldn't find key
            return prbs + 1, hits, miss + 1
        else:
            if p1 + p2 <= len(htab) - 1:
                newp1 = p1 + p2
            else:
                newp1 = p1 + p2 - (len(htab) - 1) - 1
            return probCnt(htab, ky, newp1, p2, start, prbs + 1, hits, miss)
    else:
        # if key found at index, return probes and hit, miss
        return prbs + 1, hits + 1, miss

def Search(hashTab, Ntimes, TabSize):
    # Searching
    Hitprbs, Misprbs, hit, mis = 0, 0, 0, 0
    for i in range(Ntimes):
        k = random.randint(0, 100000000)
        # First location, and second location from respective hashes
        fLoc = FHash(k, len(hashTab))
        sLoc = SecHash(k, TabSize)

        prbs, h, m = probCnt(hashTab, k, fLoc, sLoc, fLoc)
        if h != 0:
            # search hit occured, update hit and hit probes
            hit += h
            Hitprbs += prbs
        elif m != 0:
            # search miss occured, update miss and miss probes
            mis += m
            Misprbs += prbs
    print ("Searched for",Ntimes, "Hit probes", Hitprbs, "Hit", hit,
           "\n Miss probes", Misprbs, "Miss", mis)
    print ("\t",Hitprbs/hit, Misprbs/mis)
    print ("\t",Hitprbs/(hit*Ntimes), Misprbs/(mis*Ntimes))



def main():
    sys.setrecursionlimit(2000)
    LoadFactor = [0.5, 0.6666, 0.75, 0.9, 0.99]
    inputSize = 1000
    TabSize = FindNextPrime.primes(inputSize)
    keysFrom = 0
    keysTo = 2 * TabSize
    # Remove hash to choose hash type
    Type = "Double"
##    Type = "Linear"
    for loads in LoadFactor:
        hashTab = [None] * TabSize
        Num_Keys_tab = int(math.ceil(loads * float(TabSize)))
        print ("Load Factor, Data in hash table, TabSize",
               loads, Num_Keys_tab, TabSize)
        kk = 0
        while kk < Num_Keys_tab:
            k = random.randint(0, 100000000)
            first = FHash(k, TabSize)
            if hashTab[first] == None:
                hashTab[first] = k
                kk = kk + 1
            elif Type == "Double":
                second = SecHash(k, TabSize)
                sec = probes(hashTab, first, second)
                hashTab[sec] = k
                kk = kk + 1
            elif Type == "Linear":
                second = linear()
                second = probes(hashTab, first, second)
                hashTab[second] = k
                kk = kk + 1
        Ntimes = 20000
        Search(hashTab, Ntimes, TabSize)
main()
