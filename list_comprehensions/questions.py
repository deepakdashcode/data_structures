vals=[1,2,3,4,5,33,24,27,90,43,45,46,47]
mul3=[i for i in vals if i%3==0]
print(mul3)

ls=[('a',11),('b',12),('c',13)]
new_ls=[n*3 for (a,n) in ls if a =='a' or a=='b']
print(new_ls)

odd_even=['Even' if i % 2 ==0 else 'Odd' for i in range(1,10)]
print(odd_even)
