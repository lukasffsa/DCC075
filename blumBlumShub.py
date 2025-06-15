import random
from math import gcd

def bbs(p, q, iters):
    i = 0
    m = p * q
    
    # O trecho abaixo aplica o máximo divisor comum dos valores 
    while True:
        r = random.randint(1, m-1) 
        if gcd(r, m) == 1:
            break
    
    x = (r**2) % m
    bits = []
    
    # Os bits significativos são guardados abaixo
    while i < iters:
        x = (x**2) % m
        bits.append(x % 2)
        print(f"iterações concluídas: {i+1}/{iters}")
        i+=1
    
    lsb = "".join(str(bit) for bit in bits)    
    return lsb

# teste com 2 números primos grandes e 100000 iterações 
result = bbs(104511, 104723, 100000)

print(result)
