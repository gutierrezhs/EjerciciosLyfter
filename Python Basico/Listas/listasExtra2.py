my_list = [1, 2, -3, 4]
negative_numbers = 0

for number in my_list:
    if number <= 0:
         negative_numbers += 1

if negative_numbers > 0:
    print("There is at least one negative number or zero.")
else:
    print("All numbers are positive.")
    


