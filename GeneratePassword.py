import string
import random

min_length = 8
max_length = 20

name = input("What is your name: ")
print(f"Welcome to the random password generator {name}😁")

chars = 'abcdefghiklmnopqrstuvwxyz1234567890!@#$%^&*()_?.,'

number = input("How many passwords would you like to have?: ")
number = int(number)

length = input("What length would you like your password to be?: ")
length = int(length)



for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    

if len(passwords) < min_length:
    print("password short as fuck")
elif len(passwords) > max_length:
    print("password long as fuck")
else:
    print("your good to go")
    print(passwords)
