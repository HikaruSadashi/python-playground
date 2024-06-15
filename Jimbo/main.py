class Automobile:
    def __init__(self, ndoors=0, clr=""):
        self._doors = ndoors
        self._colour = clr

    def printDoors(self):
        return "Number of doors is: " + str(self._doors)

    def printColour(self):
        return "Colour is: " + self._colour

    def display(self):
        return "Car is: " + str(self._doors) + " doors, " + self._colour


class SportsCar(Automobile):
    def __init__(self, ndoors=0, clr="", eng=0):
        super().__init__(ndoors, clr)
        self._engine = eng

    def display(self):
        return super().display() + ", with " + str(self._engine) + " hp"

# Example usage
car = SportsCar(2, "Red", 300)
print(car.display())