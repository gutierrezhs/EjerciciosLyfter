def reverse_string(str):
    new_string = ""
    for character in range(len(str) - 1, -1, -1):
        new_string = new_string + str[character]

    return new_string

print(reverse_string("Hello World!"))