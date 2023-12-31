# This program generates a password for a user

from posixpath import join
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
everything_combined = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
letter_input = int(input("How many letters would you like in your password? "))
symbol_input = int(input("How many symbols would you like? "))
number_input = int(input("How many numbers would you like? "))

password = []

for l in range(letter_input):
  password += random.choice(letters)

for s in range(symbol_input):
  password += random.choice(symbols)

for n in range(number_input):
  password += random.choice(numbers)

random.shuffle(password)
new_password = "".join(password)
print(f"Here is your password: {new_password}")
