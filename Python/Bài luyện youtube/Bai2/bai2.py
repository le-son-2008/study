def sotuman(n=str):
    s=0
    for i in n: 
        s+=int(i)**3
    if s==int(n):
        return str(s)
lst=[]
lst_2=[]
for i in range(2):
    x=str(input("Nhập số hoặc dãy số cách nhau bằng dấu cách:"))
    lst.append(x)
with open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Bài luyện youtube\\Bai2\\SOTUMAN.INP","w") as f:
    for i in lst:
        f.write(i+"\n")
        inp=i.split(" ")
        for n in inp:
            if sotuman(n)==None:continue 
            else:
                lst_2.append(sotuman(n))
with open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Bài luyện youtube\\Bai2\\SOTUMAN.OUT","w") as f_2:
    for i in lst_2:
        f_2.write(i+' ')