hasValidNumber = False
while (not hasValidNumber):
    num = input("Enter a number: ")
    try:
        intInput = int(num)
    except Exception as e:
        print(f'{num} is not an invalid input! Enter a number.')
    else:
        validNumber = True
    print(f'You entered {num}')