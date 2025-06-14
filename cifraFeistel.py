def feistel(mensagem, rodadas, chave, criptografar=True):
    if len(mensagem) % 2 == 1:
        mensagem += "_"

    l = list(mensagem[:(len(mensagem) // 2)])
    r = list(mensagem[(len(mensagem) // 2):])

    chave_valores = [ord(c) for c in chave]
    tamanho_chave = len(chave_valores)
    tamanho_metade = len(l)

    for i in range(rodadas):
        subchave_idx = i if criptografar else (rodadas - 1 - i)

        # Aplica F na metade direita (criptografia) ou esquerda (descriptografia)
        alvo = r if criptografar else l
        f_output = []
        for j in range(tamanho_metade):
            k = chave_valores[(j + subchave_idx) % tamanho_chave]
            f_output.append(chr(ord(alvo[j]) ^ k))

        if criptografar:
            # Guarda L atual
            nova_l = r
            nova_r = []
            for j in range(tamanho_metade):
                nova_r.append(chr(ord(l[j]) ^ ord(f_output[j])))
        else:
            # Guarda R atual
            nova_r = l
            nova_l = []
            for j in range(tamanho_metade):
                nova_l.append(chr(ord(r[j]) ^ ord(f_output[j])))

        l, r = nova_l, nova_r

    return "".join(l + r)

mensagem_original = "PARALELEPIPEDO"
num_rodadas = 16
chave_secreta = "MINHACHAVEDESECRETA"

mensagem_criptografada = feistel(mensagem_original, num_rodadas, chave_secreta, criptografar=True)
print(f"Mensagem original:       {mensagem_original}")
print(f"Mensagem criptografada:  {mensagem_criptografada}")

mensagem_descriptografada = feistel(mensagem_criptografada, num_rodadas, chave_secreta, criptografar=False)
print(f"Mensagem descriptografada: {mensagem_descriptografada}")
