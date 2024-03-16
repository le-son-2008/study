with open("C:\\Users\\Admin\\Documents\\Code\\Python\\Bài luyện youtube\\Bai6\\UCLN.INP") as f:
    m,n=map(int,f.read().split())
def ucln_c1(m,n):
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            return str(i)
def ucln_c2(m,n):
    while m!=n:
        if m>n:m-=n
        else:n-=m
    return str(m)
with open("C:\\Users\\Admin\\Documents\\Code\\Python\\Bài luyện youtube\\Bai6\\UCLN.OUT","w") as f_2:
    f_2.write(ucln_c2(m,n))