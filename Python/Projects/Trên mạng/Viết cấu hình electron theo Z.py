def S():
	if z[0]<s and z[0] > 0 :
		a.append([b[0],s,z[0]])
		z[0] = 0
	if z[0] >= s and z[0] > 0 :
		a.append([b[0],s,s])
		z[0]-=s
		b[0]+=1
def P():
	if z[0]<p and z[0]>0:
		a.append([b[1],p,z[0]])
		z[0]=0
	if z[0]>=p and z[0]>0:
		a.append([b[1],p,p])
		z[0]-=p
		b[1]+=1
def D():
	if z[0]<d and z[0] > 0 :
		a.append([b[2],d,z[0]])
		z[0] = 0
	if z[0] >= d and z[0]>0:
		a.append([b[2],d,d])
		z[0]-=d
		b[2]+=1
def F():
	if z[0] < f and z[0] > 0 :
		a.append([b[3],f,z[0]])
		z[0] = 0
	if z[0]>=f and z[0] > 0 :
		a.append([b[3], f,f])
		z[0]-=f
		b[3]+=1

s = 2
p = 6
d = 10
f = 14
z = [int(i) for i in input("Z=").split()][0:1]
print(f"Cấu hình electron của Z={z[0]} là: ")
t = 1
a =[]
b = [1, 2, 3, 4]
c = []
d1 = []
l = {
	2:"s",
	6:"p",
	10:"d",
	14:"f",
}

for i in range(2): S()
for i in range(2): P();S()
for i in range(3): D();P();S()
for i in range(3): D(); P();S()
for i in range(4): F();D();P();S()
while (z[0]>0):
	for i in range(4): F();D();P();S()
a.sort()
for i in a:
	c.append([i[0],l.get(i[1]), i[2]])
for i in c:
	d1.append(f"{i[0]}{i[1]}{i[2]}")
print()
for i in d1:
	print(i, ",", end="")