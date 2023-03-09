from random import randint
from sys import exit
from os import system

inicio = 0
fim = 50

nSecreto = randint(inicio, fim)
tentativas = 0 
while True:
    chute = int(input("Tente um valor: "))
    if (chute == nSecreto):
        print(f"Voce acertou depois de {tentativas} tentativas")
        exit()
    elif (chute < nSecreto):
        print("Muito baixo.")
    elif (chute > nSecreto):
        print("Muito alto.")
    tentativas += 1
    system("clear")

