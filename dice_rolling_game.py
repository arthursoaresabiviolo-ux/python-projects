from random import randint

def roll_dice():
    a, b = randint(1, 6), randint(1, 6)
    return a, b

def main():
    while True:
        choice = input('Roll the dice? (y/n): ').lower()
        if choice == 'y':
            num1, num2 = roll_dice()
            print(f'Sorted numbers: {num1}, {num2}\n')
        elif choice == 'n':
            print('Thanks for playing!')
            break
        else:
            print('Invalid choice!')
        
if __name__ == '__main__':
    main()
        
