def pos(element, arr: list):
    if element < arr[0]:
        return 0
    elif element > arr[len(arr) - 1]:
        return len(arr)
    else:
        pos = -1
        for i in range(len(arr)):
            if element <= arr[i]:
                pos = i
        return pos


def shift(arr: list, pos: int):
    arr.append(None)
    for i in range(len(arr) - 2, pos - 1, -1):
        arr[i + 1] = arr[i]


ls = [10, 20, 30, 40, 50]
element = int(input('Enter the new Element\n'))
position = pos(element, ls)
print('Position is ', position)
shift(ls, position)
ls[position] = element
print(ls)
