#!/usr/bin/env python3
# This is my first attempt at creating a text based login system.
# I decided to use variables to hold the password because i don't know yet how to store passwords
# in a file or Data Base
import getpass
from time import sleep

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.03)
    print() # go to new line

print_slow('Welcome to the Mystical World of Wizardry')

print_slow('You must create an account before your adventure can begin')


print_slow("What is your character's name? (First name only): ")
while True:
    character_name = input()
    if character_name != '':
        break
    else:
        print_slow('You must identify yourself before you can enter the portal')

print_slow(f"Welcome, {character_name.title()}! Please enter the password which will secure your portal to this magical realm: ")



while True:
    user_password = getpass.getpass()
    if user_password != '':
        break
    else:
        print_slow(f"You must enter a password")

with open('passwords.txt', 'w') as opened_file:
    opened_file.write(user_password)

user_password = '' #clear password variable since no need for it and might be security risk

print_slow('Your password has successfully been forged into the Annals of Oligon')
print_slow('Enter your password to enter the Dark Realm')
user_tries = 1
total_tries = 3
while user_tries <= 3:
    tries_left = total_tries - user_tries
    user_entry = input()
    f = open("passwords.txt","r")
    lines = f.readlines()
    password = lines[0]
    if user_entry == password:
        break
    elif user_tries == 3:
        break
    else:
        if tries_left > 1:
            print_slow(f'That is incorrect. You have {tries_left} more tries until you are incinerated to ashses. Choose wisely!')
        else:
            print_slow(f'That is incorrect. You have {tries_left} more try until you are incinerated to ashses. Choose wisely!')
    user_tries += 1
    f.close()

if user_tries > 3:
    print_slow("Ha ha ha. Another poor soul has been sacrificed to the underworld")
else:
    print_slow("Welcome Warrior!")


