# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __call__(self, *args, **kwargs):
#         return self.x, self.y

# pt = Point(1,2)
# print(pt())




# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     @staticmethod
#     def area(r):
#         return 3.14 * r * r


# pt = Point(1,2)
# print(pt.area(3))



# class Student:
#     counter = 0 

#     def __init__(self, name):
#         self.name = name
#         Student.counter += 1
#         print(self.name, self.counter)


#     @classmethod
#     def show_count_student(cls):
#         print(cls.counter)


# st = Student("Alex")
# st = Student("Bob")
# Student.show_count_student()






# class Counter:
#     counter = 0 
#     def __call__(self, x):
#         Counter.counter +=x
#         return Counter.counter
    
#     def show_count(self):
#         print("qiymat",Counter.counter)

# ct = Counter()
# print(ct(3))
# print(ct(4))
# ct.show_count()

        



class Counter():
    def __init__(self):
        self.total = 0 
        self.count = 0

    def __call__(self, value):
        self.total += value
        self.count +=1
        print(self.total)

    def show_count(self):
        print(self.count) 


ct = Counter()
ct(3)         
ct(4)         
ct.show_count()    
