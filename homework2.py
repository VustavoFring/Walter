class Item:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value
    
    def __sub__(self,other):
        return self.value - other.value
    
    def __mul__(self,other):
        return self.value * other.value
    
    def __truediv__(self,other):
        return self.value / other.value

class Item2:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value
    
    def __sub__(self,other):
        return self.value - other.value
    
    def __mul__(self,other):
        return self.value * other.value
    
    def __truediv__(self,other):
        return self.value / other.value
    

item_1 = Item(5)
item_2 = Item2(3)


print(item_1 + item_2)
print(item_1 - item_2)
print(item_1 * item_2)
print(item_1 / item_2)
