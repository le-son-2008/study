import random
def doanso(tr):
    b=input('Chon do kho:')
    print("\n")
    while b!="1" and b!="2" and b!="3":
        b=input("Nhap sai roi nhap lai:")
        print("\n")
        if b=="1" or b=="2" or b=="3":break
    if b=="1":
         a=random.randrange(1,101)
         m=7
    elif b=="2":
        a=random.randrange(1,1001)
        m=10
    else:
        a=random.randrange(1,10001)
        m=13
    print("#"*40)
    print("Ban co",m,"mang")
    t=int(input('Nhap so ban cho la dung:'))
    while t!=a:
        if t<a:
            m-=1				
            print("\n")
            if m==0:
                print("#"*40)
                print("Ban da thua\nHahaha")
                print('Ket qua la:',a)
                break
            else:
                print("#"*40)
                print(">>So ban nhap nho hon roi (So ban nhap < ket qua)")
                print(">>Hay nhap so lon hon\n")
                print('Ban con',m,'mang!')
                t=int(input('Nhap lai nao:'))
        if t>a:
            m-=1
            print("\n")
            if m==0:
                print("#"*40)
                print("Ban da thua\nHahaha")
                print('Ket qua la:',a)
                break
            else:
                print("#"*40)
                print(">>So ban nhap lon hon roi (So ban nhap > ket qua)")
                print(">>Hay nhap so nho hon\n")
                print('Ban con',m,'mang!')
                t=int(input('Nhap lai nao:'))	
    if t==a:
        print("\n")
        print('>>>BAN DA THANG<<<')
print("-->>Day la tro choi doan so<<--\n")
print("Do kho                      Pham vi so\n")
print("De(7 mang)                   1-->100")
print("Binh thuong(10 mang)         1-->1.000")
print("Kho(13 mang)                 1-->10.000")
print("#"*40)

print('Chon "De" bam "1"')
print('Chon "Binh thuong" bam "2"')
print('Chon "Kho" bam "3"')
tr="Co"
while tr=="Co":
    doanso(tr)
    print("\n")
    print("Ban muon thu lai?")
    tr = input('("Co" hoac"Khong"):')
    while tr != "Co" and "Khong":
        if tr == "Khong":
            print("Tro choi ket thuc")
            break  
        print("\n")
        tr = input("Nhap sai roi, nhap lai:")