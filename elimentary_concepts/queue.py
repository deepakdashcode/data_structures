# implement queue
queue=[]
while True:
    print('Press 1 to insert element')
    print('Press 2 to delete element')
    print('Press 3 to display stack')
    choice=int(input('Enter the choice\n'))
    if choice==1:
        queue.append(int(input('Enter the element\n')))
    elif choice==2:
        if len(queue) == 0:
            print('Underflow case')
        else:
            print('Deleted element is ',queue.pop(0))
    elif choice==3:
        for i in queue:
            print(i,end=' ')
        print()

    else:
        print('Invalid input')

    if input('Enter q to exit\n').lower()[0]=='q':
        break
    else:
        continue
