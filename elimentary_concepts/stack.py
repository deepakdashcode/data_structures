# implement stack
stack=[]
while True:
    print('Press 1 to insert element')
    print('Press 2 to pop element')
    print('Press 3 to display stack')
    choice=int(input('Enter the Choice\n'))
    if choice==1:
        element=int(input('Enter the element\n'))
        stack.append(element)
    elif choice==2:
        if len(stack)==0:
            print('Underflow')
        else:
            print('Deleted element is ',stack.pop())
    elif choice==3:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
    else:
        print('Invalid input please enter correctly')

    if input('Enter q to exit\n').lower()[0] == 'q':
        break
    else:
        continue

