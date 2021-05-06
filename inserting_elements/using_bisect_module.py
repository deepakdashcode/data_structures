import bisect

ls:list=[10,20,30,40,50,60,70]
print('The List in sorted order is ',ls)
element:int=int(input('Enter the element\n'))
ind=bisect.bisect(ls,element)
bisect.insort(ls,element)
print(f'Index is {ind}')
print(ls)
