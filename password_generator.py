#Random Password Generator App v2.0
#written by Aaron Yam

import string
import random
import pyperclip

def userInput():
    try:
        passwordLength = eval(input('How many characters are in the password? '))
    except SyntaxError:
        print("Invalid input, non-integer value was entered\n")
        exit()
    except NameError:
        print("Invalid input, non-integer value was entered\n")
        exit()

    try:
        passwordOptions = input('What options would you like to include? \n\n \
    Lowercase    (abc)       (L) \n \
    Uppercase    (ABC)       (U) \n \
    Number       (123)       (N) \n \
    Symbol       (!@#$)      (S) \n \
    Punctuation  (,.{[\\]})   (A) \n \
    SELECT ALL               (Z) \n\n\
Choice(s): ')
        if not passwordOptions:
            raise ValueError("No choices were selected\n")
    except ValueError as e:
        print(e)

    passwordOptions = passwordOptions.replace(" ","").upper()
    enabledOptions = list(passwordOptions)
    userPreference = [passwordLength,enabledOptions]
    return userPreference

def generatePassword(userInputValues):
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_characters = list(string.punctuation)
    special_characters_basic = list('?!@#$%^&*()_+-=')

    lists = []
    if userInputValues[1] == []:
        exit()
    else:
        if 'Z' in userInputValues[1]:
            lists.extend((lowercase, uppercase, digits, special_characters_basic, special_characters))
        else:
            if 'L' in userInputValues[1]: lists.append(lowercase)
            if 'U' in userInputValues[1]: lists.append(uppercase)
            if 'N' in userInputValues[1]: lists.append(digits)
            if 'S' in userInputValues[1]: lists.append(special_characters_basic)
            if 'A' in userInputValues[1]: lists.append(special_characters)

    password = ""

    for characters in range(userInputValues[0]):
        characters = random.choice(random.choice(lists))
        password = password + characters

    print(password)
    pyperclip.copy(password)
    print("Password has been copied to your clipboard")
    return

def main():
    userInputValues = userInput()
    generatePassword(userInputValues)
    return

if __name__ == "__main__":
    main()
