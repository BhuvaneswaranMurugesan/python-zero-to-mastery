
class Laptop:
    
    brand = "Dell"
    
    def __init__(self):
        pass
    
    @classmethod
    def change_brand(cls,new_name):
        cls.brand = new_name

l1 = Laptop()

print(l1.brand)

l1.change_brand("HP")

print(l1.brand)
    