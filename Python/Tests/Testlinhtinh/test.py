class Bank():
    def __init__(self,hoten:str,ma_nv=int) -> None:
        self.hoten=hoten
        self.ma_nv=ma_nv

class Nhanvien(Bank):
    def __init__(self,hoten:str,ma_nv:int) -> None:
        super().__init__(
            hoten,ma_nv
        )
        self.__luong=5000000

    def get_luong(self):
        return self.__luong

    def set_luong(self,luong_moi):
        self.__luong=luong_moi

nv1=Nhanvien("Son",1234)
nv2=Nhanvien("Lam",5678)

print(nv1.get_luong())
print(nv2.get_luong())
nv2.set_luong(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
print(nv2.get_luong())