from Airport import *

class Flight:
    def __init__(self, flightNo, origAirport, destAirport):
        # Check that both origAirport and destAirport are Airport objects
        #if not isinstance(origAirport, Airport) or not isinstance(destAirport, Airport):
        #    raise TypeError("The origin and destination must be Airport objects")

        # Check the flight number format
        #if not isinstance(flightNo, str) or not re.match(r'^[A-Z]{3}\d{3}$', flightNo):
        #    raise TypeError("The flight number format is incorrect")

        self._flightNo = flightNo
        self._origin = origAirport
        self._destination = destAirport

    def __repr__(self):
        return f"Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()} [{self.isDomesticFlight() and 'domestic' or 'international'}]"

    def __eq__(self, other):
        if not isinstance(other, Flight):
            return False
        return self._origin == other._origin and self._destination == other._destination

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        return self._origin.getCountry() == self._destination.getCountry()

    def setOrigin(self, origin):
        if not isinstance(origin, Airport):
            raise TypeError("The origin must be an Airport object")
        self._origin = origin

    def setDestination(self, destination):
        if not isinstance(destination, Airport):
            raise TypeError("The destination must be an Airport object")
        self._destination = destination
