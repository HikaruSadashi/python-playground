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
        f=open(countriesFile, "r", encoding='uft8')
        for line in f:
            line = line.strip()
            parts = line.split(',')
            country = parts[0].strip()
            cont = parts[1].strip()
            self._allCountries[country]=cont
        f.close()

        f=open(airportFile, "r", encoding='uft8')
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
        f = open(flightFile, "r", encoding='utf8')
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
    
    def getAirportByCode(self, code):
        if code in self._allAirports:
            return self._allAirports[code]
        else:
            return -1

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

    def findFlightBetween(self, origAirport, destAirport):
        directFlights = self.allFlights[origAirport.getCode()]
        for flight in directFlights:
            if flight.getDestAirport() == destAirport:
                return f"Direct Flight({flight.getFlightNo()}): {origAirport.getCode()} to {destAirport.getCode()}"
        connectingAirports = set()
        for flight in directFlights:
            connectingAirport = flight.getDestAirport()
            for connectingFlight in self.allFlights[connectingAirport.getCode()]:
                if connectingFlight.getDestAirport() == destAirport:
                    connectingAirports.add(connectingAirport.getCode())
        if connectingAirports:
            return connectingAirports
        else:
            return -1
    
    def findReturnFlight(self, firstFlight):
        destAirport = firstFlight.getDestAirport()
        origAirport = firstFlight.getOrigAirport()
        for flight in self.allFlights[destAirport.getCode()]:
            if flight.getDestAirport() == origAirport:
                return flight
        return -1
    
    def findFlightsAcross(self, ocean):
        greenZone = ["Canada", "USA", "Mexico", "Brazil", "Peru"]
        redZone = ["Japan", "China", "Australia"]
        blueZone = ["UK", "France", "Germany", "Egypt", "South Africa"]
        flightsAcross = []
        for flightList in self.allFlights.values():
            for flight in flightList:
                origCountry = flight.getOrigAirport().getCountry()
                destCountry = flight.getDestAirport().getCountry()
                if (origCountry in greenZone and destCountry in redZone) or (destCountry in greenZone and origCountry in redZone):
                    if ocean == "Pacific":
                        flightsAcross.append(flight)
                elif (origCountry in greenZone and destCountry in blueZone) or (destCountry in greenZone and origCountry in blueZone):
                    if ocean == "Atlantic":
                        flightsAcross.append(flight)
        return flightsAcross

    


