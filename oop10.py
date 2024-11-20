# class Logger:
#     @staticmethod
#     def save_log():
#         print("Save log")

# class Point:
#     @staticmethod
#     def draw():
#         print("Draw")

# class InsertDatabase:
#     @staticmethod
#     def insert():
#         print("Insert Database")

# class Notebook(Point, Logger, InsertDatabase):
#     pass



# n = Notebook()
# n.draw()
# n.save_log()
# n.insert()






class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def draw():
        print("Draw")


class Logger:
    @staticmethod
    def save_log():
        print("Save log")


class Notebook(Point, Logger):
    pass



n = Notebook(1, 2)
n.draw()
n.save_log()
print(Notebook.__mro__)




