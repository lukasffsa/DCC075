#  Exercício 1 - implementação da cifra de César

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

texto_exemplo = """Explorar o universo sempre foi um dos maiores sonhos da humanidade. 
Desde os primeiros olhares para o ceu estrelado, nos perguntamos o que
existe alem do nosso planeta. Com o avancar da ciencia, enviamos sondas,
astronautas e telescopios para desvendar os misterios do cosmos. Descobrimos planetas distantes,
buracos negros e galaxias inimaginaveis. A possibilidade de vida em outros mundos nos intriga e impulsiona 
novas missoes espaciais. Empresas privadas comecam a investir em viagens espaciais comerciais, aproximando
a exploracao do espaco da realidade cotidiana. O turismo espacial, antes ficcao, ja tem data marcada para acontecer.
Marte se torna um destino possivel, e a ideia de colonizar outro planeta deixa de ser apenas teoria. 
A tecnologia avanca em ritmo acelerado, e a cada dia chegamos mais perto do desconhecido. Mas junto com o progresso vem questionamentos eticos
e ambientais. Estamos preparados para levar nossa civilizacao para fora da Terra? O futuro pode estar nas estrelas, mas depende de como cuidamos do presente. 
O espaco e um convite a sonhar, mas tambem um desafio a refletir. 
Nossa curiosidade e infinita, assim como o universo que nos cerca."""
        
    
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
frequencias = dict(sorted(frequencias.items(), key=lambda item: item[1], reverse=True))

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


freqLetrasTexto = contadorFrequencia(resultado)
freqLetrasTexto = dict(sorted(freqLetrasTexto.items(), key=lambda item: item[1], reverse=True))

print("\nFrequência das letras nas palavras em português:\n ", frequencias)
print("\nFrequência das letras no texto de exemplo:\n", freqLetrasTexto)

print("\nResultado da criptoanálise: \n")

lista_freq = list(frequencias)
lista_freq_texto = list(freqLetrasTexto)

iter = 0
while iter < len(lista_freq_texto):
    print(lista_freq_texto[iter], "corresponde a: ", lista_freq[iter])
    iter+=1
    


    
    
    
    
