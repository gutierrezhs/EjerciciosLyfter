my_list = []
my_list2 = []
word = ''
condition = True

for i in range(5):
    condition = True
    word = input("Enter a word: ")
    while condition:
        if (word == '' or word == ' '):
            print("You must enter a word.")
            word = input("Enter a word: ")
        else:
            my_list.append(word)
            condition = False

print(f"Words in the list: {my_list}")

for word in my_list:  
    if (len(word) > 4):
        my_list2.append(word)

print(f"Words with more than 4 characters: {my_list2}")

