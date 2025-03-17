import random

print("Welcome to Random password generator")
random_characters = "QWERTYUIOPASDFGHJKLZXCVBNMasdfghjklpoiuytrewqzxcvbnm1234567890!@#$%^&*+-"
no_of_passwords = int(input("Enter the number of passwords you needed:"))
password_length = int(input("Enter the number of password length you needed:"))

print("Here are your passwords:")
for x in range(no_of_passwords):
    password = ""
    for y in range(password_length):
        password = password + random.choice(random_characters)
    print(password)
