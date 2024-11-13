class Rectangle: 
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area_find(self):
        return self.__height * self.__width

    def perimetr(self):
        return (self.__height + self.__width) *2

    def is_square(self):
        return self.__height == self.__width
    
    def resize2(self, height, width):
        self.__height = height
        self.__width = width
        print(self.__height, self.__width)    

answer = Rectangle(4,74)
print(answer.area_find())
print(answer.perimetr())
print(answer.is_square())
