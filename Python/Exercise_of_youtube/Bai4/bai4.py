def prime(n):  
    if n<2:return None
    for i in range(2,n):
        if n%i==0:return None
    return True
with open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Bài luyện youtube\\Bai4\\NGUYENTO.INP","r") as f:
    n=f.read()
x=sum([int(i) for i in n])
num=prime(x)
with open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Bài luyện youtube\\Bai4\\NGUYENTO.OUT","w") as f_2:
    f_2.write(str(x)+"\n")
    if num == None:
        f_2.write("NO")
    else:
        f_2.write("YES")