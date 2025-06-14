#  Exercício 1 - implementação da cifra de César

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# A função abaixo implementa a cifra de Cesar ignorando pontuação e transforamndo todas as letras em caracteres maiúsculos:
def cifraCesar(texto, k):
    caracteres = ",.:;()-?!_"
    texto = texto.upper()
    
    for caractere in caracteres:
        texto = texto.replace(caractere, "")
        
    texto_criptografado = ""
    for char in texto:
        if char in alfabeto:
            texto_criptografado = texto_criptografado + alfabeto[((alfabeto.index(char) + k) % 26)]
    return texto_criptografado

texto_exemplo = """OXNDV, DLGQD PH LPSUHVVLRQR FRP TXDQWR WHPSR
OHYHL SUD SHUFHEHU TXH É YRFHÃ TXHP HX TXHUWR
WHU SRU SHUWR R WHPSR WRGR. YRXH É TXHP PH IDV
ULU VHP SDUDU, TXHP PH IDV IKHOCL GH YHUDGH, TXHP
PH IDV VHQWLUD PDGDGD H HVSHFLDO. DVFK TXH RX
UHDOPHQWH SUHFLVDYD GDTXHLOHVW GRLV DQRV.
HOHV IRUDP HVVHQFLDLV SUD TXH D JHQWH VH
FRQKHFHVVH GH YHUDGH, SUD TXH RX HVWLYHVVH
SURQWD SUD UHFHEHU HVVH DPRU TXH VÓ YRFH VDEH
GDU. H WDPEÉP SUD DPDU YRFH Q¾R VÓ FRPR DPLJR, PDV
FRPR SDUFHLUR. PDV LVVR Q¾R É VREUR PLP. É VREUR
YRFH, VREUR FRPR HX PH HQFDQWR FDFD GLD PDLV FRP R
VHX MHLWR GH DPDU, FRP R VHX FXLGDGR, FRP D IRMUD
TXH YRFH IDV SLDGD DWP HQIHUQWDQGR RV PDLRUHV
SUREOHPDV. DV FRLVDV SDUHFHP PDLV VLPSOHV FRP
YRFH GR PHX ODGR H, KRMH, TXDOGXH WHPSR ORQJH GH
YRFH MD Q¾R IDV PDLV VHQWLGR. WH DPR SUD VHPSUH.
"""
        
    
k = int(input("\nDigite o valor de k: "))

resultado = cifraCesar(texto_exemplo, k)

print("\nTexto criptografado:", resultado)


# Exercício 2 - implementação da criptoanálise da cifra de César:

frequencias = {
    "a" : 14.63,
    "b": 1.04,
    "c": 3.88,
    "d": 4.99,
    "e": 12.57,
    "f": 1.02,
    "g": 1.30,
    "h": 1.28,
    "i": 6.18,
    "j": 0.40,
    "k": 0.02,
    "l": 2.78,
    "m": 4.74,
    "n": 5.05,
    "o": 10.73,
    "p": 2.52,
    "q": 1.20,
    "r": 6.53,
    "s": 7.81,
    "t": 4.34,
    "u": 4.63,
    "v": 1.67,
    "w": 0.01,
    "x": 0.21,
    "y": 0.01,
    "z": 0.47

}

# A linha abaixo ordena o dicionário acima em ordem decrescente:
frequencias = dict(sorted(frequencias.items(), key=lambda item: item[1], reverse=True))

# Função abaixo conta a frequência das letras no texto criptografado e retorna um dicionário de frequências:
def contadorFrequencia(texto_criptografado):
    freq_letras = {}
    for char in texto_criptografado:
        if char in alfabeto:
            if char.lower() in freq_letras:
                freq_letras[char.lower()] += 1
            else:
                freq_letras[char.lower()] = 1
    for letra in freq_letras:
        freq_letras[letra] = round((freq_letras[letra] * 100) / len(texto_criptografado), 2)
    return freq_letras

# As duas linhas abaixo ordenam o dicionário de frequência em ordem decrescente:
freqLetrasTexto = contadorFrequencia(resultado)
freqLetrasTexto = dict(sorted(freqLetrasTexto.items(), key=lambda item: item[1], reverse=True))

print("\nFrequência das letras nas palavras em português:\n ", frequencias)
print("\nFrequência das letras no texto de exemplo:\n", freqLetrasTexto)

print("\nResultado da criptoanálise: \n")

# As duas linhas abaixo transformam os dois dicionários em listas:
lista_freq = list(frequencias)
lista_freq_texto = list(freqLetrasTexto)

# O código abaixo compara as letras mais usadas da língua portuguesa com as mais usadas na criptografia uma a uma:
iter = 0
while iter < len(lista_freq_texto):
    print(lista_freq_texto[iter], "corresponde a: ", lista_freq[iter])
    iter+=1