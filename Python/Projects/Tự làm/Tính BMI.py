#Ho tro vong lap
tr="Co"
#Tinh BMI
def bmi(kg,m):
	b=kg/(m**2)
#Dua ra ket qua
	if b<18.5:
		print("-->Ban dang nhe can")
	elif b>=18.5 and b<=22.9:
		print("-->Ban dang binh thuong")
	elif b>=23 and b<=25:
		print("-->Ban dang thua can")
	elif b>=25 and b<=29.9:
		print("!!!-->Ban bi beo phi cap do 1")
	elif b>=30 and b<40:
		print("!!!-->Ban bi beo phi cap do 2")
	else:
		print("!!!-->Ban bi beo phi cap do 3")
#Bat dau chuong trinh
while tr=="Co":
	kg=float(input(">>>Can nang cua ban(kg):"))
	m=float(input(">>>Chieu cao cua ban(m):"))
	bmi(kg,m)
#Tiep tuc hoac ket thuc chuong trinh
	print("Ban muon thu lai?")
	tr = input('("Co" hoac"Khong"):')
	while tr != "Co" and "Khong":
		if tr == "Khong":
			print("Ket thuc")
			break
		tr = input("Nhap sai roi, nhap lai:")