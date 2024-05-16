def dau(n):
    if n>0:
        return "+"+str(n)
    elif n<0:
        return str(n)
    else:
        return ""
M1=[float(i) for i in input("Tọa độ điểm thứ 1 là x,y: ").split(",")]
M2=[float(i) for i in input("Tọa độ điểm thứ 2 là x,y: ").split(",")]
a=M2[1]-M1[1]
b=-(M2[0]-M1[0])
c=a*(-M1[0]) + b*(-M1[1])
print(f"PTDT: {dau(a)}x{dau(b)}y{dau(c)}=0")