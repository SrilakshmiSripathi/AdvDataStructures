def primes(N):
    v = N
    while v <= v + 100:
        c = 2
        while c <= v - 1:
            # if a num has factor skip to next num
            if v % c == 0:
                v = v + 1
            c = c + 1
        return v

##print primes(100010)
        
