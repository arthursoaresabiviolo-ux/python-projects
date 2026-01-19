from random import choice   

choice_options = ['r', 's', 'p']
options = {'r': 'Rock', 's': 'Scissor', 'p': 'Paper'}

def get_computer_choice():
    computer_choice = choice(choice_options)
    return computer_choice

def get_user_choice():
    while True:
        user_choice = input('Rock, paper or scissor? (r/p/s): ').lower()
        if user_choice not in choice_options:
            print('Invalid choice!')
        else:
            return user_choice

def display_choice(computer_choice, user_choice):
    print(f'You chose {options[user_choice]}')
    print(f'Computer chose {options[computer_choice]}')

def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')):
        print('You win!')
    else:
        print('You lose!')

def play_game():
    while True:
        computer_choice = get_computer_choice()

        user_choice = get_user_choice()

        display_choice(computer_choice, user_choice)

        determine_winner(computer_choice, user_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

if __name__ == '__main__':
    play_game()
