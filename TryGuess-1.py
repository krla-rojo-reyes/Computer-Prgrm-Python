import random

num = random.randint(1,10)
attempts = 3
guess = ""
highVal = 10
lowVal = 1

while attempts > 0:
    print(f'\nYou have {attempts} attempts left')
    guess = input(f'Guess a number between {lowVal} to {highVal}: ')

    try:
        guess = int(guess)
        if guess <= num:
            lowVal = guess
            try:
                lowVal = int(guess)
            except:
                print(f'{guess} is an invalid input.')
        if guess == num:
            print(f'Congrats! You guessed the mystery number: {num}!')
            break
        elif guess <= num:
            attempts -= 1
            lowVal = guess + 1
            print(f'{guess} is too small!')
        elif guess >= highVal:
            print(f'{guess} is higher than guess number!')
        elif guess >= num:
            attempts -= 1
            highVal = guess - 1
            print(f'{guess} is too large!')
    except:
        print(f'{guess} is an invalid input.')

    if attempts == 0:
        print(f'\nYou ran out of attempts.\nThe mysterious number was: {num}\n')
        break

