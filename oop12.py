# from dataclasses import dataclass


# class Point:
#     def __init__(self, x, y=0):
#         self.x = x
#         self.y = y
#         self.len = (self.x +self.y) * 2



# @dataclass
# class Point2D:
#     x:int
#     y:int        


#     def __post__init__(self):
#         self.len = (self.x +self.y) * 2

# pt = Point(1,2)
# print(pt.len)
# pt2 = Point2D(2,3)
# print(pt2.len)
# # pt3 = Point2D(2,3)
# # print(pt2 == pt3)



# from dataclasses import dataclass

# class Product:
#     def __init__(self, name, price, quantity, total_value):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.total_value = total_value




# from dataclasses import dataclass



# @dataclass
# class Product:
#     name: str
#     price: float
#     quantity: int

#     def __post_init__(self):
#         self.total_value = self.price * self.quantity

# pr = Product("banana", 22.000, 4)
# print(pr)



from dataclasses import dataclass, field




@dataclass
class Example:
    a: int
    b: int = field(default = 2, compare = True)
    c: list = field(dafault_factory=list)

ex = Example(a=1, b=4, c=[3, 4, 5])
ex2 = Example(a=1, b=4, c=[3, 4, 5])





