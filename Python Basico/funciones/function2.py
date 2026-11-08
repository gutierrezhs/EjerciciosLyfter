def funtion1():
    name = "John Doe"

print(name)

#Para este caso, la variable name no es accesible fuera de la función funtion1, por lo que se generará un error al intentar imprimirla. "NameError: name 'name' is not defined"


number = 10

def funtion2():
    number = 20
    print(f'Variable number dentro de la función: {number}')

funtion2()
print(f'Variable number fuera de la función: {number}')

#para el caso de la variable number, se puede observar que dentro de la función funtion2 se crea una nueva variable number que es local a la función y al imprimir esta variable mantiene el valor dentro de la funvion, mientras que fuera de la función se mantiene el valor original de la variable number. Por lo tanto, al imprimir la variable number fuera de la función, se obtiene el valor 10.