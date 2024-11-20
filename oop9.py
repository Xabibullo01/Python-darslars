# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    

#     def __hash__(self):
#         return hash((self.x, self.y))
    

# pt = Point(1, 2)
# pt2 = Point(1, 3)
# print(hash(pt), hash(pt2))

        







###################################################

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __bool__(self):
#         print("__bool__")
#         return self.x == self.y 
    
# pt = Point(0, 0)
# if pt:
#     print("object pt give true")
# else:
#     print("false")
        







###################################################



# class Student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = list(marks)

#     def __getitem__(self, item):
#         return self.marks[item]
    
#     def __setitem__(self, key, value):
#         self.marks[key] = value

#     def __delitem__(self, key):
#         del self.marks[key]


# s1 = Student("Sergey", [5, 5, 3, 2, 5])
# print(s1[2])
# st = Student("Alex", [4,5,3,5,5])

# st.marks[3]= 4
# st[3]=4



###################################################



# class Geom:
#     name = "Geom"

#     def draw(self):
#         print("Draw geom")

# class Line(Geom):
#     name = "Line"

#     def draw(self):
#         print("Draw line")

# class Circle(Geom):
#     name = "Line"

#     def draw(self):
#         print("Circle line")




# class Line(Geom):
#     def draw(self):
#         print("Draw Line")

# class Circle(Geom):
#     name = "Circle"

#     def draw(self):




# class Product:
#     def __init__(self, name, product_id, quantity, price):
#         self.name = name
#         self.product_id = product_id
#         self.quantity = quantity
#         self.price = price

#     def __str__(self):
#         return (f"{self.name} (ID: {self.product_id}, "
#                 f"Quantity: {self.quantity}, Price: ${self.price:.2f})")


# class Warehouse:
#     def __init__(self, address):
#         self.address = address
#         self.inventory = {}

#     def add_product(self, product):
#         """Mahsulot qo'shish yoki sonini yangilash."""
#         if product.product_id in self.inventory:
#             self.inventory[product.product_id].quantity += product.quantity
#         else:
#             self.inventory[product.product_id] = product

#     def remove_product(self, product_id):
#         """Mahsulotni olib tashlash."""
#         self.inventory.pop(product_id, None)

#     def __str__(self):
#         products = "\n".join(str(product) for product in self.inventory.values())
#         return f"Warehouse at {self.address}:\n{products or 'No products'}"



# product1 = Product("Laptop", 101, 5, 999.99)
# product2 = Product("Phone", 102, 10, 599.99)

# warehouse = Warehouse("1234 Main Street")


# warehouse.add_product(product1)
# warehouse.add_product(product2)

# print(warehouse)

# warehouse.remove_product(101)

# print(warehouse)









 
        
