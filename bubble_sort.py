from random import randint

def bubble_sort(lis):
    count = 0
    rounds = 0
    while True:
        swap = False
        for i in range(len(lis) - 1 - rounds):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                swap = True
                count += 1
                print(f'{lis} --> {count}° passo')
        rounds += 1
        if not swap:
            break


def main():
    lis = [randint(1, 100) for _ in range(10)]
    print(f'{lis} --> Lista inicial')
    bubble_sort(lis)

if __name__ == '__main__':
    main()