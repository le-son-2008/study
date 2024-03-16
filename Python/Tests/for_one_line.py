lst=[1,5,8,9,3]
lst_2=[i**2 for i in lst]
print(lst_2)
lst_3=[i**2 for i in lst if i**2%2==0]
print(lst_3)
lst_4=[i for i in range(20) if i%2==0]
print(lst_4)