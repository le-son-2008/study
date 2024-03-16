def S(n):
    S=0
    for i in range(1,n+1):
        S+=1/i**2
    return str(round(S,3)).replace('.',',')
lst=[]
lst_2=[]
for i in range(2):
    n=int(input("Nhập n:"))
    lst.append(n)
    lst_2.append(S(n))
with open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Bài luyện youtube\\Bai1\\TONG.INP","w") as f:
    for i in lst:
        f.write(str(i)+"\n")
with open("C:\\Users\Admin\\Documents\\Lập trình cơ bản\\Python\\Bài luyện youtube\\Bai1\\TONG.OUT","w") as f_2:
    for i in lst_2:
        f_2.write(i+'\n')