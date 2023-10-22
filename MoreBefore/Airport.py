from Flight import *

class Airport:
    def __init__(self, code, city, country, continent):
        self._code = code
        self._city = city
        self._country = country
        self._continent = continent

    def __repr__(self):
        return f"{self._code} ({self._city}, {self._country})"

    def getCode(self):
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def getContinent(self):
        return self._continent

    def setCity(self, city):
        self._city = city

    def setCountry(self, country):
        self._country = country

    def setContinent(self, continent):
        self._continent = continent

# # --------------- Test 1 - Airport methods ---------------
# def equals (expected, student):
#     expected = expected.replace(" ", "")
#     expected = expected.replace("\t", "")
#     expected = expected.lower()
#     student = student.replace(" ", "")
#     student = student.replace("\t", "")
#     student = student.lower()
#     return expected == student


# a1 = Airport("YXU", "London", "Canada","North America")
# a2 = Airport("ABC", "Madrid", "Spain","Europe")
# a2.setCity("Athens")
# a2.setCountry("Greece")
# t1 = a1.getCode() == "YXU" and a1.getCity() == "London" and a1.getCountry() == "Canada"
# t2 = a2.getCode() == "ABC" and a2.getCity() == "Athens" and a2.getCountry() == "Greece"
# t3 = equals("YXU (London, Canada)", a1.__repr__()) and equals("ABC (Athens, Greece)", a2.__repr__())
# print('t1=',t1)
# print('t2=',t2)
# print('t2=',t3)
# if t1 and t2 and t3:
#     print("Test 1 Passed. (Airport methods)")
# else:
#     print("Test 1 Failed. (Airport methods)")

# # --------------- Test 2 - Flight methods ---------------
# a1 = Airport("YXU", "London", "Canada","North America")
# a2 = Airport("ABC", "Athens", "Greece","Europe")
# f1 = Flight("ABC123", a1, a2)
# f2 = Flight("BCS101", Airport("ABQ", "Albuquerque", "United States","North America"), Airport("OMA", "Omaha", "United States","North America"))
# f3 = Flight("XYZ321", a1, a2)
# t1 = f1.getFlightNumber() == "ABC123" and f1.getOrigin() == a1 and f1.getDestination() == a2
# t2 = f1 != f2 and f1 == f3
# t3 = equals("Flight(ABC123): London -> Athens [international]", f1.__repr__()) and equals("Flight(BCS101): Albuquerque -> Omaha [domestic]", f2.__repr__())
# t4 = not(f1.isDomesticFlight()) and f2.isDomesticFlight()

# if t1 and t2 and t3 and t4:
#     print("Test 2 Passed. (Flight methods)")
# else:
#     print("Test 2 Failed. (Flight methods)")