def linear_search(element, ls):
    ind = -1
    for i in range(0, len(ls)):
        if ls[i] == element:
            ind = i
            break
    return ind


ls = []
n=int(input('Enter the number of elements\n'))

for i in range(0,n):
    ls.append(int(input(f'Enter element {i}\n')))
while True:
    element=int(input('Enter the elements to be searched\n'))
    ind=linear_search(element,ls)
    if ind==-1:
        print('Element not found')
    else:
        print(f'Element found at index {ind}')

    if input('Enter q to exit\n').lower()[0]=='q':
        break
    else:
        continue
