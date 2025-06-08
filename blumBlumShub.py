import random
from math import gcd

def bbs(p, q, iters):
    i = 0
    m = p * q
    
    while True:
        r = random.randint(1, m-1) 
        if gcd(r, m) == 1:
            break
    
    x = (r**2) % m
    bits = []
    
    while i < iters:
        x = (x**2) % m
        bits.append(x % 2)
        print(f"iterações conclídas: {i+1}/{iters}")
        i+=1
    
    lsb = "".join(str(bit) for bit in bits)    
    return lsb

result = bbs(104511, 104723, 100000)

print(result)
