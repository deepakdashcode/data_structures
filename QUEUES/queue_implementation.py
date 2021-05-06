queue = []


def dequeue(qu: list):
    if len(qu) == 0:
        print('Underflow Case')
    else:
        print('Deleted element is ', qu.pop(0))


def enqueue(qu: list):
    element = int(input('Enter the number to be inserted : '))
    qu.append(element)


def peek(qu: list):
    if len(qu) != 0:
        print('Front element is ', qu[0])


def Display(qu: list):
    if len(qu) == 0:
        print('Empty Queue')
    elif len(qu) == 1:
        print(qu[0], '<-- Front and Rear End')
    else:
        for i in range(0, len(qu)):
            if i == 0:
                print(qu[i], '<-- Front End')
            elif i == len(qu) - 1:
                print(qu[i], '<-- Rear End')
            else:
                print(qu[i])


while True:
    print('1 for Enqueue')
    print('2 for Dequeue')
    print('3 for Peek')
    print('4 for Display')
    print('5 for Exit')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        enqueue(queue)
    elif choice == 2:
        dequeue(queue)
    elif choice == 3:
        peek(queue)
    elif choice == 4:
        Display(queue)
    elif choice == 5:
        break
    else:
        print('Invalid Input')
