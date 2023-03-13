"""Jogo de adivinhação numérica com escalonamento logarítmico de dificuldade."""
from random import randint
from sys import exit
from os import system, name
from math import log
from time import sleep

def resetaVariaveis():
    """Reinicializa variáveis para uma nova partida."""
    global limite, nSecreto, tentativas, nivel
    limite = 2
    nSecreto = randint(0, limite)
    tentativas = round(log(limite, 2))
    nivel = 0

limite = 2
nSecreto = randint(0, limite)
tentativas = round(log(limite, 2))
nivel = 0
print(f"\nNÍVEL {nivel}")
while True:
    print(f"{tentativas} tentativa(s) restante(s)")
    chute = int(input(f"Tente um valor de 0 a {limite}: "))
    if (chute == nSecreto):
        # Inicializa variáveis para o próximo nível
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
            print("Suas chances acabaram",
            f"O número secreto é {nSecreto}",
            sep="\n")
            sleep(2)
            resetaVariaveis()
            system("cls")
            print(f"\nNÍVEL {nivel}")

