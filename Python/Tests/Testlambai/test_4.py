def q(lst):
    for i in range(len(lst)):
        s=0
        d=0
        for j in range(i,len(lst)):
            s+=lst[j]
            d+=1
        if s==0:
            return d