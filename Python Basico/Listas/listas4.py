my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_even = []

for par in my_list:
    if par % 2 == 0:
        list_even.append(par)

print(list_even)