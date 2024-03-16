def prime(i):  
    if i<2:return False
    for j in range(2,i):
        if i%j==0:return False
    return True
with open("C:\\Users\\Admin\\Documents\\Code\\Python\\Bài luyện youtube\\Bai7\\NGUYENTO.INP") as f:
    n=int(f.readline())
    lst=list(map(int,f.readline().split()))
#C1
s=0
for i in range(n):
    if prime(lst[i]):
        s+=1
#C2
lst_nt=[i for i in lst if prime(i)]
with open("C:\\Users\\Admin\\Documents\\Code\\Python\\Bài luyện youtube\\Bai7\\NGUYENTO.OUT","w") as f_2:
    f_2.write(str(len(lst_nt)))