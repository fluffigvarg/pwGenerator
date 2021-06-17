#! python3
# pwGenerator.py - Generate a strong password based on your inputs.

import string, random, pyperclip

def pwGenerator(length, caps, num, symbol):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = '!@#$%^&*'
    pwList = [lower]
    if caps:
        pwList.append(upper)
    if num:
        pwList.append(numbers)
    if symbol:
        pwList.append(symbols)

    passwordRaw = []

    # Password generation
    for i in range(length):
        currentList = pwList[random.randint(0, len(pwList)-1)]
        passwordRaw.append(currentList[random.randint(0, len(currentList)-1)])

    return ''.join(passwordRaw)

def useCharacter(character_type):
    active = True
    while active:
        status = input(f'Do you want to use {character_type}? (y/n) ')
        if status == 'y':
            return True
        elif status == 'n':
            return False
        else:
            print('Invalid input, try again.')

def pwLength():
    active = True
    while active:
        length = int(input('How many characters do you want in the password? '))
        if length < 8:
            print('Password too short, pick between 8 and 128.')
        elif length > 128:
            print('Password too long, pick between 8 and 128.')
        else:
            active = False
            return length


active = True
while active:
    length = pwLength()
    caps = useCharacter('caps')
    num = useCharacter('numbers')
    symbols = useCharacter('symbols')
    newPassword = pwGenerator(length, caps, num, symbols)
    print(newPassword)
    pyperclip.copy(newPassword)
    print('Password copied to clipboard!')
    repeat = input('Would you like to create another? (y/n) ')
    if repeat == 'y':
        continue
    if repeat == 'n':
        break