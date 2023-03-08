from os import system
from random import randint

inicio = 0
fim = 50

nSecreto = randint(inicio, fim)
tentativas = 1 
while True:
    nJogador = int(input("Tente um valor: "))
    if (nJogador == nSecreto):
        print(f"Voce acertou depois de {tentativas} tentativas")
        break
    elif (nJogador < nSecreto):
        print("Muito baixo.")
    elif (nJogador > nSecreto):
        print("Muito alto.")
    tentativas += 1
    system("clear")

