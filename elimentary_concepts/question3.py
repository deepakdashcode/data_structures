def INSERTQ(Arr: list):
    data=int(input('Enter the element\n'))
    Arr.append(data)

def DELETEQ(Arr: list):
    if len(Arr)==0:
        print('Underflow')
    else:
        Arr.pop(0)



