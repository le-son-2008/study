#Bai 5: Bac THang
def check(n):
    if len(n)>1:
        for i in range(-1,len(n)-1):
            if n[i] > n[i+1]:
                return True
    return False
fi=open('step.inp')
fo=open('step.out','w')
n=int(fi.readline())
a=[int(i) for i in fi.readline().split()]
d=0
for i in a:
    lst=[int(_) for _ in str(i)]
    print(lst)
    if check(lst):d+=1
print(d,file=fo)
fi.close()
fo.close()