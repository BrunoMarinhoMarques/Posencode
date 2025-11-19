from util import *

continuar = True
while continuar!=False:
 desenha_logo()       
 texto = input("\n\nDigite o texto que será codificado (não pode ter acento): ")
 codificador_randomico = random_excesso()
 resultado_criptografado = criptografia(texto, codificador_randomico)
 resposta = input("Gostaria de ver a mensagem criptografada? | 1 - SIM | 2 - NÃO |\n")
 if resposta=="1":
  print("Mensagem criptografada: ", resultado_criptografado)
  resposta = input("Gostaria de descriptografar a mensagem? | 1 - SIM | 2 - NÃO |\n")
  if resposta =="1":
    resultado = descriptografia(resultado_criptografado, codificador_randomico)
    print("Mensagem descriptografada: ", resultado)
    continuar = input("Gostaria de continuar criptografando? | 1 - SIM | 2 - NÃO | \n")
    if continuar == "1":
        continuar = True
      
      
    else:
        print("Até breve!")
        continuar = False    
  else:
    print("Até Breve!")
    continuar = False
 else:
  resposta = input("Gostaria de descriptografar a mensagem? | 1 - SIM | 2 - NÃO | \n")
  if resposta=="1":
    resultado = descriptografia(resultado_criptografado, codificador_randomico)
    print(f"Mensagem descriptografada: {resultado}")
    continuar = input("Gostaria de continuar criptografando? | 1 - SIM | 2 - NÃO | \n")
    if continuar == "1":
        continuar = True
      
    else:
        continuar = False
        print("Até Breve!")
  else:
     continuar = False
     print("Até Breve!")
