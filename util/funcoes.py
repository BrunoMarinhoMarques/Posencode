import time
import sys

def random_excesso():
    tempo = int(__import__("time").time() * 1000000)
    M = 2**31
    X0 = tempo % M
    A = 15
    B = 13
    X1 = (A * X0 + B) % M
    R1 = X1 / M
    num = int(R1 * 100) % 10
    return num


def criptografia(texto,codificador):
    texto_criptografado = ""
    lista_texto_criptografado = ""
    for caracter in texto:
        texto_criptografado += chr(ord(caracter) + codificador)
        lista_texto_criptografado = list(texto_criptografado)
    loading()
    resultado_final = inversao_caracteres(lista_texto_criptografado)
    return resultado_final

def inversao_caracteres(posicoes):
 for i in range(1, len(posicoes), 2):
    posicoes[i], posicoes[i-1] = posicoes[i-1], posicoes[i]

    resultado = "".join(posicoes)
    return resultado





def loading():
    segundos=2
    print("Carregando", end="")
    for _ in range(segundos):
        print(".", end="")
        sys.stdout.flush()  # força a impressão imediata
        time.sleep(1)
    print("\nConcluído!")

def descriptografia(texto,codificador):
    texto_descriptografado = ""
    for caracter in texto:
        texto_descriptografado += chr(ord(caracter) - codificador)
    loading()
    return texto_descriptografado


def desenha_logo():
    print("\n\n\n")
print(" ██████   ██████  ███████ ███████ ███    ██  ██████  ██████  ██████  ███████ ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
print(" ██   ██ ██    ██ ██      ██      ████   ██ ██      ██    ██ ██   ██ ██      ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
print(" ██████  ██    ██ ███████ █████   ██ ██  ██ ██      ██    ██ ██   ██ █████   ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
print(" ██      ██    ██      ██ ██      ██  ██ ██ ██      ██    ██ ██   ██ ██      ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
print(" ██       ██████  ███████ ███████ ██   ████  ██████  ██████  ██████  ███████ ")   