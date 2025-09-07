## Password Generator Project ##
import random
letters=[
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

symbols=[
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '`', '~'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

## Easy Level ##
    # print("Welcome to PyPassword Generator!")
    # letters1=int(input("How many letters would you like in your password?\n "))
    # symbols1=int(input("How many symbols would you like?\n"))
    # numbers1=int(input("How many numbers would you like?\n "))

    # password=""

    # for char in range(1,letters1+1):
    #     random_char=random.choice(letters)
    #     password+=random_char

    # for char in range(1,symbols1+1):
    #     random_char=random.choice(symbols)
    #     password+=random_char

    # for char in range(1,numbers1+1):
    #     random_char=random.choice(numbers)
    #     password+=random_char

    # password1=random.choice(password)
    # print(password1)

## Hard Way ##
print("Welcome to PyPassword Generator!")
letters1=int(input("How many letters would you like in your password?\n "))
symbols1=int(input("How many symbols would you like?\n"))
numbers1=int(input("How many numbers would you like?\n "))

password_list=[]

for char in range(1,letters1+1):
    password_list.append(random.choice(letters))

for char in range(1,symbols1+1):
    password_list.append(random.choice(symbols))

for char in range(1,numbers1+1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for str in password_list:
    password+=str
print(f"your password is: {password}")
