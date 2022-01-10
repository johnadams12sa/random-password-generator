#random password generator app
#written by Aaron Yam

import string
import random

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = list(string.punctuation)
special_characters_basic = list('!@#$%^&*()"')
#lists = [lowercase, uppercase, digits, special_characters, special_characters_basic]

passwordLength = eval(input('How many characters are in the password? '))
passwordOptions = input('What options would you like to include? \n\n \
Lowercase    (abc)       (L) \n \
Uppercase    (ABC)       (U) \n \
Number       (123)       (N) \n \
Symbol       (!@#$)      (S) \n \
Punctuation  (,.{[\\]})   (A) \n \
SELECT ALL               (Z) \n\n\
Choice(s): ')

passwordOptions = passwordOptions.replace(" ","").upper()
enabledOptions = list(passwordOptions)
lists = []
if enabledOptions == []:
    exit()
else:
    if 'Z' in enabledOptions:
        lists.extend((lowercase, uppercase, digits, special_characters_basic, special_characters))
    else:
        if 'L' in enabledOptions: lists.append(lowercase)
        if 'U' in enabledOptions: lists.append(uppercase)
        if 'N' in enabledOptions: lists.append(digits)
        if 'S' in enabledOptions: lists.append(special_characters_basic)
        if 'A' in enabledOptions: lists.append(special_characters)

password = ""

for characters in range(passwordLength):
    characters = random.choice(random.choice(lists))
    password = password + characters

print(password)
