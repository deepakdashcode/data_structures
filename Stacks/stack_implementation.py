stack=[]

while True:
    print('STACK OPERATIONS')
    print('1 Push')
    print('2 Pop')
    print('3 Peek')
    print('4 Display')
    print('5 Exit')
    print()
    print('......................')
    print()
    try:
        choice = int(input('Enter the choice: '))
        if choice == 1:
            element = int(input('Enter the element to push : '))
            stack.append(element)
        elif choice == 2:
            if len(stack) != 0:
                print('Element deleted is ', stack.pop())
            else:
                print('Underflow')
        elif choice == 3:
            if len(stack)!=0:
                print('Element at the top of stack is : ', stack[len(stack) - 1])
            else:
                print('Empty stack')
        elif choice == 4:
            for i in range(len(stack) - 1, -1, -1):
                if i==(len(stack)-1):
                    print(stack[i],'<-- top')
                else:
                    print(stack[i])
        elif choice==5:
            print('Exiting Now.......')
            break
        else:
            print('Invalid input')

    except ValueError as e:
        print('Error Code : ', e)
        continue
