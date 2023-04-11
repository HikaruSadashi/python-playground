from Flight import *
from Airport import *

class Aviation:
    def __init__(self):
        self._allAirports={}
        self.allFlights={}
        self.allCountries={}

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
    except:
        return False
    return True

