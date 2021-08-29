import random

alphabets = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
numbers = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]
characters = [ "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "~", "+", "=", "-", "_", "?", "<", ">" ]

print ("Welcome to the password generator!")
alps = int(input("Enter the number of alphabets to be used: "))
nums = int(input("Enter the number of numbers to be used: "))
chars = int(input("Enter the number of characters/symbols to be used: "))

password_list = []

for _ in range(alps):
    password_list.append(random.choices(alphabets))

for _ in range(nums):
    password_list.append(random.choices(numbers))

for _ in range(chars):
    password_list.append(random.choices(characters))

random.shuffle(password_list)

password = ""
for val in range(len(password_list)):
    password += str(password_list[val][0])

print (f"Generated psssword is: {password}")

