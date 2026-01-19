from random import randint

number_to_guess = randint(1, 50)
attempts = 0

while True:
    try:
        number_typed_by_user = int(input('Guess the number between 1 and 50: '))
        if number_typed_by_user == number_to_guess:
            attempts += 1
            print('Congratulations! You guessed the number.')
            print(f'You took {attempts} attempts!')
            break
        elif number_typed_by_user > 50 or number_typed_by_user < 1:
            print('Invalid number! You must type a number between 1 and 50.\n')
        else:
            if number_typed_by_user > number_to_guess:
                print('Too high! Try again.\n')
            elif number_typed_by_user < number_to_guess:
                print('Too low! Try again.\n')
            attempts += 1
    except ValueError:
        print('Please enter a valid number.\n')



