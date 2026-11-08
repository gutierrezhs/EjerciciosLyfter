employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

employees_in_ventas = []
employees_in_ti = []
employees_in_rrhh = []

for employee in employees:
    if employee['department'] == 'Ventas':
        employees_in_ventas.append(employee)
    elif employee['department'] == 'TI':
        employees_in_ti.append(employee)
    elif employee['department'] == 'RRHH':
        employees_in_rrhh.append(employee)


print("Empleados en Ventas:", employees_in_ventas)
print("Empleados en TI:", employees_in_ti)
print("Empleados en RRHH:", employees_in_rrhh)