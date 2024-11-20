# 2
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def info(self):
        print(f"Name: {self.name}")

class Flyable:
    def __init__(self, wing_span: float):
        self.wing_span = wing_span

    def fly(self):
        print("Flying with a wingspan of", self.wing_span, "meters.")

class Swimmable:
    def __init__(self, swimming_speed: int):
        self.swimming_speed = swimming_speed

    def swim(self):
        print("Swimming at a speed of", self.swimming_speed, "km/h.")



class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name, species, wing_span, swimming_speed):
        Animal.__init__(self, name, species)
        Flyable.__init__(self, wing_span)
        Swimmable.__init__(self, swimming_speed)

    def quack(self):
        print("Quack! Quack!")

class Pinguin(Animal, Swimmable):
    def __init__(self, name, species, swimming_speed):
        Animal.__init__(self, name, species)
        Swimmable.__init__(self, swimming_speed)

    def slide(self):
        print("Sliding on ice!")




kavalskiy = Pinguin(name="Kavalskiy", species="Bird", swimming_speed=15)


kavalskiy.info()
print("Species:", kavalskiy.species)
print("Swimming Speed:", kavalskiy.swimming_speed)
kavalskiy.swim()
kavalskiy.slide()

