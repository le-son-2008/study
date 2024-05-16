import pandas as pd

# nhập danh sach từ bàn phím
f=open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Tests\\sinhvien.txt","a",encoding="utf-8")
while True:
    maSV= input("nhập mã SV: ")
    if maSV =="":
        break
    tenSV =input("Tên Sinh viên: ")
    Lop= input("lớp : ")
    Que = input("Quê quán: ")

    f.write("\t".join([maSV,tenSV,Lop,Que]) + "\n")
f.close()

f=open("C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Tests\\sinhvien.txt","r",encoding="utf-8")
print("\t".join([" Mã SV"," Tên SV","Lớp "," Quê"]))
for sv in f.readlines():
    print(sv.replace("\n",""))
f.close()

f="C:\\Users\\Admin\\Documents\\Lập trình cơ bản\\Python\\Tests\\sinhvien.txt"
SV=pd.read_csv(f,sep="\t",names=["Mã SV","Tên SV","Lớp","Quê"])
print(SV)

DSSV_lop=SV.sort_values(["Quê"])
print(DSSV_lop)

DSSV_a2=SV.query('Lớp=="10a2"')
print(DSSV_a2)