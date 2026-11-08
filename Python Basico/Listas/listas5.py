my_list = []

print("Ingrese 10 números enteros:")

for i in range(10):
    i = int(input(f"Número {i + 1}: "))
    my_list.append(i)
    
highest_number = my_list[0] 
for i in my_list:
    if i > highest_number:
        highest_number = i

print(f'{my_list}. El más alto fue: {highest_number}')