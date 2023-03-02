from decimal import Decimal

peso = Decimal(input("Insira um peso (kg): "))
altura = Decimal(input("Insira uma altura (m): "))
imc = peso / (altura ** 2)

print(f"\nIMC é {imc:.2f}: ", end="")
if (imc <= 18.5):
    print("Abaixo do peso normal")
elif (imc > 18.5) and (imc <= 25):
    print("Peso normal")
elif (imc > 25) and (imc <= 30):
    print("Acima do peso normal")
else:
    print("Obesidade")

