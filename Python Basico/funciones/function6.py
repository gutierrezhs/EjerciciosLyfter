def sort_string(string):
    new_string = string.split("-")
    new_string.sort()
    new_string = "-".join(new_string)
    return new_string


result = sort_string("python-variable-funcion-computadora-monitor")

print(f"The sorted string is: {result}")