my_list = [10, 2, 30, 20, 50, 60, 70, 80, 90, 100]
new_list = []
total_sum = 0
average = 0

if len(my_list) == 0:
    print("The list is empty.")
    exit()  

for number in my_list:
    total_sum = total_sum + number

average = total_sum / len(my_list)

for number in my_list:
    if number > average:
        new_list.append(number)

print("Average:", average)
print(f"New List:  {new_list}")