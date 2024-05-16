from math import sqrt
tof="tiep"
while tof=="tiep":
	b=[float(i) for i in input("Nhap day so (cach nhau bang MOT dau cach): ").split(" ")]
	tb=sum(b)/len(b)
	print('Trung bing cong cua day so la:',tb)
	_=0
	for i in b:
		_+=(i-tb)**2
	ps=_/len(b)
	dlc=sqrt(ps)
	print("Phương sai: ",ps)
	print("Độ lệch chuẩn: ",dlc)
	tof=input('"tiep" hay "khong"?\nNhap vao day:').lower()
	if tof != "tiep" and tof != "khong":
		tof=input("Sai roi nhap lai:")
else:print("Xong")