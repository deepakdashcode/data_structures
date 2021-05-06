def MakePush(Package):
    element=input('Enter the package description\n')
    Package.append(element)

def MakePop(Package):
    if len(Package)==0:
        print('Package empty ... underflow case')
    else:
        print('Element deleted is ',Package.pop())







