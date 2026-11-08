#Cree un programa que le pida tres números al usuario y muestre el mayor.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

print("El mayor número es:", mayor) 