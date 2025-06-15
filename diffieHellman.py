def mod_exp(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# parâmetros públicos
p = 23
g = 5

# chaves privadas
ana = 6
joao = 15

# trocam as chaves públicas
A = mod_exp(g, ana, p)
B = mod_exp(g, joao, p)

# calculam o segredo compartilhado
s_ana = mod_exp(B, ana, p)
s_joao = mod_exp(A, joao, p)

print("Compartilhamento de segredo")
print(f"p = {p}, g = {g}")
print(f"Ana envia A = {A}")
print(f"João envia B = {B}\n")

print(f"Ana calcula s = {s_ana}")
print(f"João calcula s = {s_joao}\n")

if s_ana == s_joao:
    print(f"Sucesso! Segredo comum = {s_ana}")
else:
    print("Erro: segredos diferentes")
