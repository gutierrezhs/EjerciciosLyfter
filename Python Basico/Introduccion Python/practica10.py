# Dada n cantidad de notas de un estudiante, calcular:
# 1.- Cuantas notas tiene aprobadas (mayor a 70).
# 2.- Cuantas notas tiene desaprobadas (menor a 70).
# 3.- El promedio de todas.
# 4.- El promedio de las aprobadas.
# 5.- El promedio de las desaprobadas.

grade_counter = 1
number_of_passing_grades = 0
number_of_failing_grades = 0
average_of_passing_grades = 0
average_of_failing_grades = 0
overall_average_grade = 0

total_number_of_notes = int(input("Ingrese la cantidad de notas: "))

if total_number_of_notes <= 0:
    print("La cantidad de notas debe ser mayor a 0")
else:
    while (grade_counter <= total_number_of_notes):
        current_note = float(input(f"Ingrese la nota {grade_counter}: "))
        if current_note < 70:
            number_of_failing_grades = number_of_failing_grades + 1
            average_of_failing_grades = average_of_failing_grades + current_note
        else:
            number_of_passing_grades = number_of_passing_grades + 1
            average_of_passing_grades = average_of_passing_grades + current_note

        overall_average_grade = overall_average_grade + (current_note /     total_number_of_notes)
        grade_counter = grade_counter + 1

    if number_of_failing_grades !=0:
        average_of_failing_grades = average_of_failing_grades / number_of_failing_grades
        print(f"El estudiante tiene esta cantidad de notas desaprobadas: {number_of_failing_grades}")
        print(f"Este es el promedio de notas desaprobadas: {average_of_failing_grades}")
            
        
    if number_of_passing_grades !=0:
        average_of_passing_grades = average_of_passing_grades / number_of_passing_grades
        print(f"El estudiante tiene esta cantidad de notas aprobadas: {number_of_passing_grades}")
        print(f"Este es el promedio de notas aprobadas: {average_of_passing_grades}")
  
    print(f"Este es el promedio total de notas: {overall_average_grade}")



