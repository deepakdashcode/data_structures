ls = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 32, 43, 45, 78, 778]


def binary(element, ls):
    ls.sort()
    lower = 0
    higher = len(ls)-1
    ind = -1
    while lower <= higher:
        mid_ind = (lower + higher) // 2
        middle_element = ls[mid_ind]
        if element == middle_element:
            ind = mid_ind
            break
        if element > middle_element:
            lower = mid_ind + 1
        if element < middle_element:
            higher = mid_ind - 1
    return ind


print(binary(element=779, ls=ls))
