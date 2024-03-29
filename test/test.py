#Random Password Generator App v2.0
#written by Aaron Yam

import string
import random
import os
import pyperclip

def userInput():
    passwordLengthInputBool = True
    while(passwordLengthInputBool):
        try:
            passwordLength = eval(input('How many characters are in the password? '))
            if passwordLength < 0:
                raise InputValueError
            passwordLengthInputBool = False
        except SyntaxError:
            print("Invalid input, non-integer value was entered\n")
            continue
        except NameError:
            print("\nInvalid input, non-integer value was entered\n")
            continue
        except InputValueError:
            print("Invalid input, enter a positive value\n")

    passwordOptionsInputBool = True
    while(passwordOptionsInputBool):

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
                raise ValueError("\nNo choices were selected\n")
                continue
            for char in passwordOptions:
                if char.isalpha() != True:
                    raise ValueError("\nAn invalid choice was entered\n")
                    continue
                if char not in ['l','u','n','s','a','z','L','U','N','S','Z']:
                    raise ValueError("\nAn invalid choice was entered\n")
                    continue
            

            passwordOptionsInputBool = False
        except ValueError as e:
            print(e)
            continue

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

def welcomeMessage():
    print('The Password Generator App\n\n ')
    return

def requestContinuePrompt():
    requestContinuePromptResponse = input('Generate another password? [Y/N] \n')
    requestContinueValid = True
    while requestContinueValid:
        if requestContinuePromptResponse[0] == 'y':
            return True
        elif requestContinuePromptResponse[0] == 'n':
            return False
        else:
            print("Your input seemed a bit odd, please try again? \n \n")
            
def clean():
    # For Windows
    if os.name == 'nt':
        os.system('cls')


    # For macOS and Linux
    else:
        os.system('clear')

def main():
    welcomeMessage()
    continueAppUse = True
    while(continueAppUse):
        userInputValues = userInput()
        generatePassword(userInputValues)
        continueAppUse = requestContinuePrompt()
        clean()
    return

if __name__ == "__main__":
    main()