from Flight import *
from Airport import *

class Aviation:
    def __init__(self):
        self._allAirports={}
        self._allFlights={}
        self._allCountries={}

    # Getters
    def getAllAirports(self):
        return self._allAirports
    
    def getAllFlights(self):
        return self._allFlights
    
    def getAllCountries(self):
        return self._allCountries
    
    # Setters
    def setAllAirports(self, allAirports):
        self._allAirports = allAirports
    
    def setAllFlights(self, allFlights):
        self._allFlights = allFlights
    
    def setAllCountries(self, allCountries):
        self._allCountries = allCountries

    def loadData(self,airportFile, flightFile, countriesFile):
        f=open(countriesFile, "r")
        for line in f:
            line = line.strip()
            parts = line.split(',')
            country = parts[0].strip()
            cont = parts[1].strip()
            self._allCountries[country]=cont
        f.close()

        f=open(airportFile, "r")
        for line in f:
            line = line.strip()
            parts = line.split(',')
            code = parts[0].strip()
            country = parts[1].strip()
            city = parts[2].strip()
            cont= self._allCountries[country]
            newAirport = Airport(code,city,country,cont)
            self._allAirports[code] = newAirport
        f.close()


        for key in self._allAirports:
            self._allFlights[key] = []
        f = open(flightFile, "r")
        for line in f:
            line = line.strip()
            parts = line.split(',')
            no = parts[0].strip()
            origCode = parts[1].strip()
            destCode = parts[2].strip()
            origObj = self._allAirports[origCode]
            destObj = self._allAirports[destCode]
            newFlight = Flight(no,origObj,destObj)
            self._allFlights[origCode].append(newFlight)
        f.close()

        return True
    
    def getAirportByCode(self, code):
        if code in self._allAirports:
            return self._allAirports[code]
        else:
            return -1

    # ============================
    def findAllCityFlights(self, city):
        flights = []
        for key in self._allAirports:
            airport = self._allAirports[key]
            if airport.getCity() == city:
                for flight in self._allFlights[key]:
                    flights.append(flight)
        return flights

    def findFlightByNo(self, flightNo):
        for key in self._allAirports:
            for flight in self._allFlights[key]:
                if flight.getFlightNo() == flightNo:
                    return flight
        return -1

    def findAllCountryFlights(self, country):
        flights = []
        for key in self._allAirports:
            airport = self._allAirports[key]
            if airport.getCountry() == country:
                for flight in self._allFlights[key]:
                    flights.append(flight)
            elif airport.getContinent() == country:
                for flight in self._allFlights[key]:
                    flights.append(flight)
        return flights

    # Might have to regenerate
    def findFlightBetween(self, origAirport, destAirport):
        if destAirport in self._allFlights[origAirport.getCode()]:
            return f"Direct Flight({self._allFlights[origAirport.getCode()][destAirport.getIndex()].getFlightNo()}): {origAirport.getCode()} to {destAirport.getCode()}"
        else:
            connecting_airports = set()
            for flight in self._allFlights[origAirport.getCode()]:
                x = flight.getDestination()
                if x != destAirport:
                    for flight2 in self._allFlights[x.getCode()]:
                        if flight2.getDestination() == destAirport:
                            connecting_airports.add(x.getCode())
            if len(connecting_airports) > 0:
                return connecting_airports
            else:
                return -1

    def findReturnFlight(self, firstFlight):
        for flight in self.allFlights[firstFlight.getDestination().getCode()]:
            if flight.getDestination() == firstFlight.getOrigin():
                return flight
        return -1

    def findFlightsAcross(self, ocean):
        crossings = []
        if ocean == "Atlantic":
            for flight in self.allFlights.values():
                for f in flight:
                    origin_continent = f.getOrigin().getContinent()
                    dest_continent = f.getDestination().getContinent()
                    if origin_continent == "North America and South America" and dest_continent == "Europe and Africa":
                        crossings.append(f)
                    elif origin_continent == "Europe and Africa" and dest_continent == "North America and South America":
                        crossings.append(f)
        elif ocean == "Pacific":
            for flight in self.allFlights.values():
                for f in flight:
                    origin_continent = f.getOrigin().getContinent()
                    dest_continent = f.getDestination().getContinent()
                    if origin_continent == "North America and South America" and dest_continent == "Asia and Australia":
                        crossings.append(f)
                    elif origin_continent == "Asia and Australia" and dest_continent == "North America and South America":
                        crossings.append(f)
        return crossings
    

    # def findFlightBetween(self, origAirport, destAirport):
    #     directFlights = self._allFlights[origAirport.getCode()]
    #     for flight in directFlights:
    #         if flight.getDestAirport() == destAirport:
    #             return f"Direct Flight({flight.getFlightNo()}): {origAirport.getCode()} to {destAirport.getCode()}"
    #     connectingAirports = set()
    #     for flight in directFlights:
    #         connectingAirport = flight.getDestAirport()
    #         for connectingFlight in self._allFlights[connectingAirport.getCode()]:
    #             if connectingFlight.getDestAirport() == destAirport:
    #                 connectingAirports.add(connectingAirport.getCode())
    #     if connectingAirports:
    #         return connectingAirports
    #     else:
    #         return -1
    
    # def findReturnFlight(self, firstFlight):
    #     destAirport = firstFlight.getDestAirport()
    #     origAirport = firstFlight.getOrigAirport()
    #     for flight in self.allFlights[destAirport.getCode()]:
    #         if flight.getDestAirport() == origAirport:
    #             return flight
    #     return -1
    
    # def findFlightsAcross(self, ocean):
    #     greenZone = ["Canada", "USA", "Mexico", "Brazil", "Peru"]
    #     redZone = ["Japan", "China", "Australia"]
    #     blueZone = ["UK", "France", "Germany", "Egypt", "South Africa"]
    #     flightsAcross = []
    #     for flightList in self.allFlights.values():
    #         for flight in flightList:
    #             origCountry = flight.getOrigAirport().getCountry()
    #             destCountry = flight.getDestAirport().getCountry()
    #             if (origCountry in greenZone and destCountry in redZone) or (destCountry in greenZone and origCountry in redZone):
    #                 if ocean == "Pacific":
    #                     flightsAcross.append(flight)
    #             elif (origCountry in greenZone and destCountry in blueZone) or (destCountry in greenZone and origCountry in blueZone):
    #                 if ocean == "Atlantic":
    #                     flightsAcross.append(flight)
    #     return flightsAcross



    
# # # --------------- Test 4 - loadData() ---------------

# avi = Aviation()

# flightsFileName = "flights.txt"

# t1 = avi.loadData("airports.txt", flightsFileName, "countries.txt")
# total = 0


# #print(avi.getAllFlights())

# for i in avi._allFlights:
#     total += len(avi._allFlights[i])

# print("Result: " + str(len(avi._allAirports)))
# # Okay debug all conditions good except t1 is not 37

# if t1 and len(avi._allAirports) == 37 and total == 60:
#     print("Test 4 Passed. (loadData())")
# else:
#     print("Test 4 Failed. (loadData())")


# --------------- Test 6 - findAllCityFlights() ---------------
avi = Aviation()
flightsFileName = "flights.txt"

avi.loadData("airports.txt", flightsFileName, "countries.txt")

cf = avi.findAllCityFlights("Toronto")

#print(cf)

cfs = ""
for f in cf:
    cfs += f.getFlightNumber() + " "

#print(cfs) # MCK533 QGC143 KPP582 CFE916
# Missing 2 light nums
# CUN974
# AOK874

t1 = isinstance(cf,list) and len(cf) == 6
acodes = ['MCK533','QGC143','KPP582','CUN974','CFE916','AOK874 ']

total = 0
for a in acodes:
    if a in cfs:
        total += 1
t2 = total == 6

#print(total) # 4

if t1 and t2:
    print("Test 6 Passed. (findAllCityFlights())")
else:
    print("Test 6 Failed. (findAllCityFlights())")