ls=[1,2,3,4,10,20,30,45,50,70,90,100]
def binary_search(element:int , ls: list):
    lower=0
    upper=len(ls)-1
    while lower <= upper:
        middle=(lower+upper)//2
        if element == ls[middle]:
            return middle
        elif element > ls[middle]:
            lower=middle+1
        else:
            upper=middle-1
    return -1

print(binary_search(45,ls))