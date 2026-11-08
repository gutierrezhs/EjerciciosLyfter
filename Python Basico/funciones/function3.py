my_list = [4,6,2,29]

def sum_list(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

print(sum_list(my_list))