tof="tiep"
while tof=="tiep":
	b=[int(i) for i in input("Nhap day so (cach nhau bang MOT dau cach): ").split(" ")]
	print('Trung bing cong cua day so la:',sum(b)/len(b))
	tof=input('"tiep" hay "khong"?\nNhap vao day:').lower()
	while tof != "tiep" and tof != "khong":
		tof=input("Sai roi nhap lai:")
else:print("Xong")