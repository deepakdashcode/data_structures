# rows=int(input('Enter the number of rows : '))
# columns=int(input('Enter the number of columns : '))
# arr=[]
# for i in range(0,rows):
#     current_row = []
#     for j in range(0,columns):
#         element=int(input(f'Enter the element of row {i+1} and column {j+1} : '))
#         current_row.append(element)
#     arr.append(current_row)

# Traversing a 2D list

# Method 1

# arr=[[10, 20], [30, 40], [50, 60]]
# print('[')
# for row in arr:
#     print('\t[ ',end='')
#     for j in row:
#         print(j,end=' ')
#     print(']')
# print(']')

# Method 2

arr=[[10, 20], [30, 40], [50, 60]]
rows=len(arr)
cols=len(arr[0])
print('[')
for i in range(rows):
    print('\t[ ', end='')
    for j in range(cols):
        print(arr[i][j], end=' ')
    print(']')
print(']')
