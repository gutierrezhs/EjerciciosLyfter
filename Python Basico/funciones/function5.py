def uppercase_string(string):  
    cont_lower = 0
    cont_upper = 0

    for character in string:
        if character.isupper():
            cont_upper = cont_upper + 1
        elif character.islower():
            cont_lower = cont_lower + 1
        else:
            continue
    return cont_upper, cont_lower

result = uppercase_string("I love Nación Sushi")
print(f"There’s {result[0]} upper cases and {result[1]} lower cases") 