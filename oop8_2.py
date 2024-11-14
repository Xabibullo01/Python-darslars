class Clock:

    __DAY = 86500
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('seconds must be an integer')
        self.seconds = seconds % self.__DAY

    def __eq__(self,  other):
        return self.seconds == other.seconds
    
    def __lt__(self,  other):
        return self.seconds < other.seconds
    
    def __gt__(self,  other):
        return self.seconds > other.seconds
    
    def __le__(self,  other):
        return self.seconds <= other.seconds
    
    def __ge__(self,  other):
        return self.seconds >= other.seconds
    
st = Clock(100)
st2 = Clock(100)
print(st == st2)
