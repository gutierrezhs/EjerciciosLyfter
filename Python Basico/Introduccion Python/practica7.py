# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
# Bebé: 0-2 años
# Niño: 3-12 años
# Preadolescente: 13-15 años
# Adolescente: 16-19 años
# Adulto joven: 20-39 años
# Adulto: 40-64 años
# Adulto mayor: 65+ años

name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))   

if (age > 0 and age <= 2):
    category = "Bebé"
elif (age >= 3 and age <= 12):
    category = "Niño"
elif (age >= 13 and age <= 15):
    category = "Preadolescente"
elif (age >= 16 and age <= 19):
    category = "Adolescente"
elif (age >= 20 and age <= 39):
    category = "Adulto joven"
elif (age >= 40 and age <= 64):
    category = "Adulto"
else:
    category = "Adulto mayor"

print(f"{name} {last_name}, {age} años, es un {category}.")