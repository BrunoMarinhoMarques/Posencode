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
    for caracter in texto:
        texto_criptografado += chr(ord(caracter) + codificador)
    loading()
    return texto_criptografado


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