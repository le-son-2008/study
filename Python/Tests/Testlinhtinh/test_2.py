class Item(): 
    def __init__(self, name:str, price:float, quantity=0): 
        self.name = name 
        self.price = price 
        self.quantity = quantity 
        assert price>=0,f"{price} o hop le, phai >0"
        assert quantity>=0,f"{quantity} o hop le, phai >0"
 # khởi tạo phương thức
    def Tong_gia(self):
        return self.price * self.quantity
    @staticmethod
    def Check_gia(gia):
        if gia<=500:
            return "Cheap,tầng 1"
        else:
            return "Expensive,tầng 2"
class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0,type="4G"):
        super().__init__(name,price,quantity)
        self.type=type
item1 = Item("Tivi",5000,2) 
item2 = Item("Laptop",3000,2)
item3 = Item("Mac",3000)
item4 = Phone("Phone 1",2000,5,"5G")
item5 = Phone("Phone 2",1500,4)
print(item1.Check_gia(item1.Tong_gia()))