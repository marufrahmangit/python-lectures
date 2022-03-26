import random

def get_guess():
    return list(input('What is your guess: '))

def generate_code():
    digits = []
    for num in range(10):
        digits.append(str(num))
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code, user_guess):
    if code == user_guess:
        return 'CODE CRACKED'

    clues = []
    i = 0
    for num in user_guess:
        if num == code[i]:
            clues.append('Match')
        elif num in code:
            clues.append('Close')
        i = i + 1

    if clues == []:
        return ['Nope']
    else:
        return clues

print('welcome to test')

secret_code = generate_code()

clue_report = []

while clue_report != 'CODE CRACKED!':
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print('Here is the result of your guess')
    for clue in clue_report:
        print(clue)