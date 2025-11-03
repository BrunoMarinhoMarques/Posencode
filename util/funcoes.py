import time
import sys

def random_excesso():
    num=0
    while(num==0):
        tempo = int(__import__("time").time() * 1000000)
        M = 2**31
        X0 = tempo % M
        A = 15
        B = 13
        X1 = (A * X0 + B) % M
        R1 = X1 / M
        num = int(R1 * 100) % 10
    return num

def criar_arquivo_texto(texto):
    arquivo = open('arquivo.txt', 'w', encoding='utf-8')
    arquivo.write(texto)
    arquivo.close()



 

def criptografia(texto,codificador):
    texto_original = ""
    texto_criptografado = ""
    lista_texto_criptografado = ""
    for caracter in texto:
          if(ord(caracter) + codificador >= 127):
              texto_criptografado += chr((ord(caracter) - 95) + codificador)
              lista_texto_criptografado = list(texto_criptografado)
          else: 
            texto_criptografado += chr(ord(caracter) + codificador)
            lista_texto_criptografado = list(texto_criptografado)
         
    loading()
    resultado_final = inversao_caracteres(lista_texto_criptografado)
    criar_arquivo_texto(resultado_final)
    return resultado_final




def descriptografia(texto,codificador):

    texto_criptografado = ""
    lista_texto_criptografado = ""
    for caracter in texto:
          if(ord(caracter) - codificador < 32):
              texto_criptografado += chr((ord(caracter) + 95) - codificador)
              lista_texto_criptografado = list(texto_criptografado)
          else: 
            texto_criptografado += chr(ord(caracter) - codificador)
            lista_texto_criptografado = list(texto_criptografado)
    loading()
    resultado_final = inversao_caracteres(lista_texto_criptografado)
    return resultado_final


def inversao_caracteres(posicoes):
 for i in range(1, len(posicoes), 2):
    posicoes[i], posicoes[i-1] = posicoes[i-1], posicoes[i]

 resultado = "".join(posicoes)
 return resultado

def inversao_caracteres_descriptografar(posicoes):
 for i in range(1, len(posicoes), 2):
    posicoes[i-1], posicoes[i] = posicoes[i], posicoes[i-1]

    resultado = "".join(posicoes)
 return resultado



def loading():
    segundos=3
    print("Carregando", end="")
    for _ in range(segundos):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(1)
    print("\nConcluído!")


def desenha_logo():
    print("\n\n\n")
print(" ██████   ██████  ███████ ███████ ███    ██  ██████  ██████  ██████  ███████ ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
print(" ██   ██ ██    ██ ██      ██      ████   ██ ██      ██    ██ ██   ██ ██      ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
print(" ██████  ██    ██ ███████ █████   ██ ██  ██ ██      ██    ██ ██   ██ █████   ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
print(" ██      ██    ██      ██ ██      ██  ██ ██ ██      ██    ██ ██   ██ ██      ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
print(" ██       ██████  ███████ ███████ ██   ████  ██████  ██████  ██████  ███████ ")   