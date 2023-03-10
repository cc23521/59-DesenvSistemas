from random import randint
from sys import exit
from os import system, name
from math import log

verde = "\033[1;32m"
vermelho = "\033[1;31m"
preto = "\033[0m"

# Jogo de adivinhação com escalonamento exponencial de dificuldade
limite = 2
nSecreto = randint(0, limite)
tentativas = round(log(limite, 2))
nivel = 0
while True:
    print(f"{tentativas} tentativa(s) restante(s)")
    chute = int(input(f"Tente um valor de 0 a {limite}: "))
    if (chute == nSecreto):
        continuar = input(f"{verde}Deseja jogar o próximo nível? [s/n] {preto}")
        if (continuar == 'n'):
            exit()
        else:
            # Inicia uma nova partida
            limite *= 2
            nSecreto = randint(0, limite)
            tentativas = round(log(limite, 2))
            nivel += 1
            system("clear" if name == "posix" else "cls")
            print(f"NÍVEL {nivel}")
    else:
        tentativas -= 1
        if (tentativas):
            if (chute < nSecreto):
                print("Muito baixo.")
            else:
                print("Muito alto.")
        else:
            print(f"{vermelho}Suas chances acabaram{preto}")
            print(f"{vermelho}O número secreto é {nSecreto}{preto}")
            exit()

