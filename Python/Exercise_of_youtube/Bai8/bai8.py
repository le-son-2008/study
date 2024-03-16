with open("C:\\Users\\Admin\\Documents\\Code\\Python\\Bài luyện youtube\\Bai8\\DAYXN.INP") as f:
    x,n=map(int,f.read().split())
def f(x):
    return sum([int(i)**2 for i in str(x)])
with open("C:\\Users\\Admin\\Documents\\Code\\Python\\Bài luyện youtube\\Bai8\\DAYXN.OUT","w") as f_2:
    for i in range(n):
        f_2.write(str(x)+' ')
        x=f(x)