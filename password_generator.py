import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '?']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Python Password Generator!!")
num_of_letters = int(input("How many letters you want in your password?\n"))
num_of_symbols = int(input("How many symbols you want in your password?\n"))
total_numbers = int(input("How many numbers you want in your password?\n"))

total_characters = num_of_letters + num_of_symbols + total_numbers

easy_password = ''
hard_password = ''

# Easy version
# for char in range(1, (num_of_letters + 1)):
#     index = random.randint(0, len(letters)-1)
#     easy_password += letters[index]
#
# for char in range(1, (num_of_symbols + 1)):
#     index = random.randint(0, len(symbols)-1)
#     easy_password += symbols[index]
#
# for char in range(1, (total_numbers + 1)):
#     index = random.randint(0, len(numbers)-1)
#     easy_password += numbers[index]
#
# print(easy_password)

# Hard version
list_of_character = []

for char in range(1, (num_of_letters + 1)):
    choice = random.choice(letters)
    list_of_character.append(choice)

for char in range(1, (num_of_symbols + 1)):
    choice = random.choice(symbols)
    list_of_character.append(choice)

for char in range(1, (total_numbers + 1)):
    choice = random.choice(numbers)
    list_of_character.append(choice)

random.shuffle(list_of_character)

for char in list_of_character:
    hard_password += char

print(f'Your generated password is: {hard_password}')