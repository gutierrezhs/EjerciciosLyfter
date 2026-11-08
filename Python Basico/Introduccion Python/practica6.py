# Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
#     Si le salen errores, no se asuste. Lealos e intente comprender qué significan.
#     Los errores son oportunidades de aprendizaje.
#     Por ejemplo:
#           string + string → ?
#           string + int → ?
#           int + string → ?
#           list + list → ?
#           string + list → ?
#           float + int → ?
#           bool + bool → ?

name = "Juan"
age = 25
is_student = False
grades = [8, 9, 7]
salary = 1500.56

#print(name + name)              
#print(name + age)              
#print(age + name)              
#print(grades + grades)        
#print(name + grades)           
#print(salary + age)            
#print(salary + is_student)    
print(is_student + salary)  


#Line 19 - Resultado: JuanJuan
#Line 20 - Resultado: TypeError: can only concatenate str (not "int") to str
#Line 21 - Resultado: TypeError: unsupported operand type(s) for +: 'int' and 'str'
#Line 22 - Resultado: [8, 9, 7, 8, 9, 7]
#Line 23 - Resultado: TypeError: can only concatenate str (not "list") to str
#Line 24 - Resultado: 1525.56
#Line 25 - Resultado: 1500.56
#Line 26 - Resultado: 1500.56