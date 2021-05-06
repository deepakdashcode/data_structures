# Method 1
# ls=[]
# for i in [1,3,5]:
#     for j in [2,5,8]:
#         ls.append(i*j)
# print(ls)

# Output [2, 5, 8, 6, 15, 24, 10, 25, 40]

# Method 2

# ls=[i*j for i in [1,3,5] for j in [2,5,8]]
# print(ls)
#

################################################################################################

# Method 1
# ls=[(x,y) for x in range(15) if x%2==0 for y in range(15) if y%2==1]
# print(ls)
#
# Method 2

ls=[]
 

