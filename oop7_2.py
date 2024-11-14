class Number:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Number({self.value})"

    def __len__(self):
        return len(str(abs(self.value)))

    def __abs__(self):
        return abs(self.value)

num = Number(-127)

print('str',str(num))        
print('repr',repr(num))     
print('len',len(num))      
print('abs',abs(num))      
