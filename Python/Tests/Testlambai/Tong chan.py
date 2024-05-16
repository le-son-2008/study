with open("C:\\Users\\Administrator\\OneDrive\\Desktop\\Code\\Python\\Tests\\Testlambai\\TOMGCHAN.INP") as f:
    n=int(f.readline())
    lst=map(int,f.readline().split())
with open("C:\\Users\\Administrator\\OneDrive\\Desktop\\Code\\Python\\Tests\\Testlambai\\TOMGCHAN.OUT","w") as f_2:
    s=0
    for i in lst:
        if i%2==0:
            print(i,file=f_2)
            s+=i
    print(s,file=f_2)