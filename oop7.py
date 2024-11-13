# # 1
# class Cat:
#     def __init__(self, name):
#         self.name = name


#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
    
#     def __str__(self):
#         return f"{self.name}"
    

# ct = Cat("Alex")
# print(ct.__repr__)


# # 2
# class Point:
#     def __init__(self, *args):
#         self.__coorgs = args

#     def __len__(self):
#         return len(self.__coorgs)
    
#     def __abs__(self):
#         return list(map(abs, self.__coorgs))
    

# pt = Point(1, 2, 3, 4, 5, 6)
# print(len(pt))


# list1 = [1, -2, 3, -4, 5, -6, -7]
# res = list(map(abs, list1))
# print(res)

