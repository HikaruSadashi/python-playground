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
            
            
            # WE DETECT 6 HERE so line detects
            
            self._allFlights[origCode].append(newFlight)

            #if origCode == "YYZ" or destCode == "YYZ":
                #print("Toronto detected!!")
                #print(newFlight)
        f.close()

        return True
    
    def getAirportByCode(self, code):
        if code in self._allAirports:
            return self._allAirports[code]
        else:
            return -1

    
    def findAllCityFlights(self, city):
        flights = []

        for key in self._allAirports:
    
            # Append any flights with same inCode
            for flight in self._allFlights[key]:
                if flight.getDestination().getCity() == city or flight.getOrigin().getCity() == city:
                    flights.append(flight)

        return flights

    # this one not tested?
    def findFlightByNo(self, flightNo):
        # for key in self._allAirports:
        #     for flight in self._allFlights[key]:
        #         if flight.getFlightNo() == flightNo:
        #             return flight

        for key in self._allAirports:
    
            # Append any flights with same inCode
            for flight in self._allFlights[key]:
                if flight.getFlightNumber() == flightNo:
                    return flight
                    
        return -1

    # ============================
    def findAllCountryFlights(self, country):
        #print(self._allFlights)

        flights = []

        #Iterate on every airport using keys from airport dict
        for key in self._allAirports:

            #get current airport
            airport = self._allAirports[key]

            #if airport country is the one we are looking for
            if airport.getCountry() == country:

                # look for flights with the same key
                for flight in self._allFlights[key]:
                    flights.append(flight)

            # do the same for continent here
            elif airport.getContinent() == country:
                for flight in self._allFlights[key]:
                    flights.append(flight)




            # ANOTHER IMPLEMENTION
            for flight in self._allFlights[key]:

                destination = flight.getDestination()
                descontinent = destination.getContinent()
                descountry = destination.getCountry()

                if descountry == country or descontinent == country:
                    flights.append(flight)
            #     origin = flight.getOrigin()
            #     origin.getContinent()
            #     origin.getCountry()
                
                print(flights)
                
        return flights

    def findFlightBetween(self, origAirport, destAirport):
        
        directFlightDestinations = []
        directFlights = []

        # Check for direct flights in a list of flights with the given origin aiport key or code
        for flight in self._allFlights[origAirport.getCode()]:
            
            #Add to a list if there is a direct flight
            if flight.getDestination() == destAirport:
                directFlightDestinations.append(flight.getDestination())
                directFlight = flight
        
        #statement = destAirport in directFlights
        #print(statement)
        
        if destAirport in directFlightDestinations:
            return f"Direct Flight({directFlight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"
            #print("Interesting")
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
    
    # Direct Flight(MTN376): PVG to YOW

    
    def findReturnFlight(self, firstFlight):

        #print(type(firstFlight))

        for flight in self._allFlights[firstFlight.getDestination().getCode()]:
            if flight.getDestination() == firstFlight.getOrigin():
                return flight
        return -1

    # for flight in self._allFlights.values():
    #             for f in flight:
    #                 origin_continent = f.getOrigin().getContinent()
    #                 dest_continent = f.getDestination().getContinent()
    #                 if origin_continent == "North America and South America" and dest_continent == "Europe and Africa":
    #                     crossings.append(f)
    #                 elif origin_continent == "Europe and Africa" and dest_continent == "North America and South America":
    #                     crossings.append(f)
    # =================================================================================
    def findFlightsAcross(self, ocean):

        crossings = set()
        AmericasOrigin = False
        AsiaAustraliaOrigin = False
        EuropeAfricaOrigin = False

        AmericasDest = False
        AsiaAustraliaDest = False
        EuropeAfricaDest = False

        for flight in self._allFlights.values():

            for f in flight:

                origin_continent = f.getOrigin().getContinent()
                dest_continent = f.getDestination().getContinent()
                flightCode = f.getFlightNumber()
                
                # Classifys which continent the origin is from based on the country
                AmericasOrigin =  origin_continent == "North America" or origin_continent == "South America"
                EuropeAfricaOrigin =  origin_continent == "Europe" or origin_continent == "Africa"
                AsiaAustraliaOrigin = origin_continent == "Australia" or origin_continent == "Asia"
                

                # Classifys which continent the dest is from based on the country
                AmericasDest =  dest_continent == "North America" or dest_continent == "South America"
                EuropeAfricaDest =  dest_continent == "Europe" or dest_continent == "Africa"
                AsiaAustraliaDest =  dest_continent == "Australia" or dest_continent == "Asia"
                    
                
                if ocean == "Atlantic":
                    # Append flight if Atlantic
                    # print("Atlantic")/Reached here

                    if (AmericasOrigin and EuropeAfricaDest) or (AmericasDest and EuropeAfricaOrigin):

                        crossings.add(flightCode)

                        # Debug code
                        # print("FlightCode: " + flightCode)
                        # print("Origin: " + origin_continent)
                        # print("Dest: " + dest_continent)
                        # print(" ")
                
                if ocean == "Pacific":
                    # not triggered, good

                    # Append flight if Pacific
                    if (AmericasOrigin and AsiaAustraliaDest) or (AmericasDest and AsiaAustraliaOrigin):
                        crossings.add(flightCode)
                        
                        # # Debug code
                        # print("FlightCode: " + flightCode)
                        # print("Origin: " + origin_continent)
                        # print("Dest: " + dest_continent)
                        # print(" ")
                    
                    
                    
        if not crossings:
            return -1
        else:
            return crossings
    
    # Atlantic
    # res == {'XJX595', 'LJC201', 'DAJ762', 'MDW532', 'YZF667', 'JAG578', 'JKQ130', 'JHW048', 'YFZ738', 'CUN974', 'NIA196', 'VKG041', 'VIP930', 'YOF338', 'USO770', 'USO771'}
    # Set ^

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



# # --------------- Test 7 - findAllCountryFlights() ---------------

# avi = Aviation()
# flightsFileName = "flights.txt"

# avi.loadData("airports.txt", flightsFileName, "countries.txt")
# cf = avi.findAllCountryFlights("Brazil")

# #print(cf)

# cfs = ""

# for f in cf:
#     cfs += f.getFlightNumber() + " "
# t1 = isinstance(cf,list) and len(cf) == 4
# acodes = ['YZF667','XGY802','MOO674','FFC468 ']
# total = 0
# for a in acodes:
#     if a in cfs:
#         total += 1
# t2 = total == 4

# if t1 and t2:
#     print("Test 7 Passed. (findAllCountryFlights())")
# else:
#     print("Test 7 Failed. (findAllCountryFlights())")

# --------------- Test 8 - findFlightBetween() ---------------

# avi = Aviation()
# flightsFileName = "flights.txt"

# def equals (expected, student):
#     expected = expected.replace(" ", "")
#     expected = expected.replace("\t", "")
#     expected = expected.lower()
#     student = student.replace(" ", "")
#     student = student.replace("\t", "")
#     student = student.lower()
#     return expected == student

# avi.loadData("airports.txt", flightsFileName, "countries.txt")

# f1 = avi.findFlightBetween(avi.getAirportByCode("PVG"), avi.getAirportByCode("YOW"))
# # -1
# #print(f1)



# f2 = avi.findFlightBetween(avi.getAirportByCode("LAX"), avi.getAirportByCode("DTW"))
# # -1 (right output)
# #print(f2)

# #Custom code
# f3 = avi.findFlightBetween(avi.getAirportByCode("LAX"), avi.getAirportByCode("DTW"))
# # -1 (right output)
# print(f3)

# t1 = equals(f1, "Direct Flight(MTN376): PVG to YOW")
# t2 = f2 == -1

# if t1 and t2:
#     print("Test 8 Passed. (findFlightBetween())")
# else:
#     print("Test 8 Failed. (findFlightBetween())")


# # --------------- Test 10 - findReturnFlight() ---------------

# avi = Aviation()
# flightsFileName = "flights.txt"

# def equals (expected, student):
#     expected = expected.replace(" ", "")
#     expected = expected.replace("\t", "")
#     expected = expected.lower()
#     student = student.replace(" ", "")
#     student = student.replace("\t", "")
#     student = student.lower()
#     return expected == student

# # LOD619,MEX,LAX
# # LOX618,LAX,MEX

# # USO770,MEX,CPT
# # USO771,CPT,MEX

# #EKR896,SFO,YHZ

# avi.loadData("airports.txt", flightsFileName, "countries.txt")

# # Find a flight object to input
# f1 = avi.findFlightByNo('LOD619') 
# print(f1) 
# #[Flight(LOD619): Mexico City -> Los Angeles [international]]

# f2 = avi.findFlightByNo('USO770')
# f3 = avi.findFlightByNo('EKR896')

# # # First use of function here
# t1 = avi.findReturnFlight(f1)
# print(t1)

# t1 = avi.findReturnFlight(t1)
# t2 = avi.findReturnFlight(f2)
# t2 = avi.findReturnFlight(t2)
# t3 = avi.findReturnFlight(f3)

# if f1 == t1 and f2 == t2 and t3 == -1:
#     print("Test 10 Passed. (findReturnFlight())")
# else:
#     print("Test 10 Failed. (findReturnFlight())")



# --------------- Test 11 - findFlightsAcross() ---------------

avi = Aviation()
flightsFileName = "flights.txt"

def equals (expected, student):
    expected = expected.replace(" ", "")
    expected = expected.replace("\t", "")
    expected = expected.lower()
    student = student.replace(" ", "")
    student = student.replace("\t", "")
    student = student.lower()
    return expected == student

# -----

# avi.loadData("airports.txt", flightsFileName, "countries.txt")

# res=avi.findFlightsAcross('Atlantic') #Tested pacific too
# #print(res) # Empty 

# if res == {'XJX595', 'LJC201', 'DAJ762', 'MDW532', 'YZF667', 'JAG578', 'JKQ130', 'JHW048', 'YFZ738', 'CUN974', 'NIA196', 'VKG041', 'VIP930', 'YOF338', 'USO770', 'USO771'}:
#     print("Test 11 Passed. (findFlightsAcross('Atlantic'))")
# else:
#     print("Test 11 Failed. (findFlightsAcross('Atlantic'))")

# Passed?
# But the printed ones wrong?

# # --------------- Test 12 - findFlightsAcross() ---------------
avi.loadData("airports.txt", flightsFileName, "countries.txt")
res=avi.findFlightsAcross('Pacific')
if res == {'MTN376', 'QMG091', 'VDT680', 'CSY487', 'YOI104', 'TYV528', 'KPP582', 'CSX772', 'ERO171', 'PGY075', 'YVF322', 'EYS649'}:
    print("Test 12 Passed. (findFlightsAcross('Pacific'))")
else:
    print("Test 12 Failed. (findFlightsAcross('Pacific'))")
