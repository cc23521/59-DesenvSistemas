from random import randint
from sys import exit
from os import system, name
from math import log
from time import sleep

# Jogo de adivinhação com escalonamento exponencial de dificuldade
limite = 2
nSecreto = randint(0, limite)
tentativas = round(log(limite, 2))
nivel = 0
while True:
    print(f"{tentativas} tentativa(s) restante(s)")
    chute = int(input(f"Tente um valor de 0 a {limite}: "))
    if (chute == nSecreto):
        continuar = input(f"Deseja jogar o próximo nível? [s/n] ")
        if (continuar == 'n'):
            system("cls")
            exit()
        else:
            # Inicia uma nova partida
            limite *= 2
            nSecreto = randint(0, limite)
            tentativas = round(log(limite, 2))
            nivel += 1
            system("cls")
            print(f"NÍVEL {nivel}")
    else:
        tentativas -= 1
        if (tentativas):
            if (chute < nSecreto):
                print("Muito baixo.")
            else:
                print("Muito alto.")
        else:
            print(f"Suas chances acabaram")
            print(f"O número secreto é {nSecreto}")
            sleep(2)
            limite = 2
            nSecreto = randint(0, limite)
            tentativas = round(log(limite, 2))
            nivel = 0
            system("cls")
            print(f"NÍVEL {nivel}")
