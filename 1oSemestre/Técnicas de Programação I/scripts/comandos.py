num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

while True: 
  op = int(input("""Escolha uma operação
Soma: 1
Subtração: 2
Multiplicação: 3
Divisão: 4
> """))
  if op in range(1,5):
    break
  else:
    print("Operação inválida, tente novamente.")

if op == 1:
  print(num1 + num2)
elif op == 2:
  print(num1 - num2)
elif op == 3:
  print(num1 * num2)
else:
  print(num1 / num2)