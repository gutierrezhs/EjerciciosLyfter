my_list = []
number_to_find = 0
number = 1


print("Introduzca una lista de numeros enteros, si quiere finalizar agregue un 0 al final de la lista.")
while number != 0:
    number = int(input("Ingrese un numero (0 para terminar): "))
    if number == 0:
        break
    my_list.append(number)

if my_list:
    number_to_find = int(input("Ingrese el numero a buscar:"))
else:
    print("No se ingreso ningun numero a la lista, por lo tanto no se puede buscar un numero.")
    exit()

print(f"Lista ingresada: {my_list}")

for number in my_list:
    if number_to_find == number:
        print(f"El numero {number_to_find} se encuentra en la lista.")
        break

        

