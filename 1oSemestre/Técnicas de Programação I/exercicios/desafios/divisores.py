"""Determina os divisores de um número qualquer e se este é primo."""
num = int(input("Insira um numero qualquer: "))

divisores = []
for divisor in range(1, num // 2):
    if (num % divisor == 0):
        divisores.append(divisor)
divisores.append(num)

# Checa se a metade do número inserido também é divisor
if (num % (num // 2) == 0):
    divisores.insert(-1, num // 2)

if len(divisores) == 2:
    print(f"{num} é primo") 

print(divisores)
