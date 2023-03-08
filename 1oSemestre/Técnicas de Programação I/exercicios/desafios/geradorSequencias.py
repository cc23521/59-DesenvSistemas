inicio = int(input("Insira o valor inicial da sequencia: "))
fim = int(input("Insira o valor final da sequencia: "))
step = int(input("Insira o intervalo entre cada elemento: "))

print("[ ", end="")
if (inicio < fim):
    while (inicio <= fim):
        print(inicio, end=" ")
        inicio += step
elif (inicio > fim):
    while (inicio >= fim):
        print(inicio, end=" ")
        inicio -= step
else:
    print(" ", end="") 
print("]")

