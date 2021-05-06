from math import factorial, pi, pow, sin

# ls = [2,4,6,8,10]
# Without Condition
# Method 1
# ls=[]
# for i in range(1,6):
#     ls.append(i*2)
# print(ls)

# Method 2
# ls=[i*2 for i in range(1,6)]
# print(ls)


# With condition
# ls=[]
# for i in range(1,50):
#     if i % 7 == 0:
#         ls.append(i)
# print(ls)
#

# def my_sin(x):
#     if x==0:
#         return 0.0
#     if x==pi/2:
#         return 1.0
#
#     no_of_terms=10
#     sign=+1
#     sum=0
#     for i in range(0,no_of_terms+1):
#         power=(2*i )+1
#         new_value=(x**power)/(factorial(power))
#         sum=sum+(sign*new_value)
#
#         sign=sign*(-1)
#     return sum


ls = [i for i in range(1, 50) if i % 7 == 0]
ls1 = [i if i % 7 == 0 else i + 1 for i in range(1, 50)]
print(ls1)
print(ls)
