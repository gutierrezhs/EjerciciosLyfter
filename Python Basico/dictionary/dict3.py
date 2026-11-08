list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

print(employee)
for key in list_of_keys:
    if key in employee:
        employee.pop(key)
    else:
        print(f"{key} not found in employee dictionary.")

print(employee)
