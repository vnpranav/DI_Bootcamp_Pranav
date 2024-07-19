class Airline:
    def __init__(self, id, name):
        self.id = id  # Two letters code
        self.name = name
        self.planes = []  # List of Airplanes belonging to this airline

    def __repr__(self):
        return f"Airline(id={self.id}, name={self.name})"
    
class Airplane:
    def __init__(self, id, airline):
        self.id = id
        self.current_location = None  # Airport where the airplane is currently located
        self.company = airline  # Airline object
        self.next_flights = []  # List of Flights, sorted by datetime

    def fly(self, destination):
        # Make the airplane take off and land if a flight is scheduled for this destination
        for flight in self.next_flights:
            if flight.destination == destination:
                flight.take_off()
                self.current_location = flight.destination
                flight.land()
                break

    def location_on_date(self, date):
        # Returns where the plane will be on this date
        for flight in self.next_flights:
            if flight.date == date:
                return flight.destination
        return None

    def available_on_date(self, date, location):
        # Returns True if the plane can fly from this location on this date
        # It can fly if it is in this location on this date and if it doesn’t already have a flight planned
        if self.current_location != location:
            return False
        for flight in self.next_flights:
            if flight.date == date:
                return False
        return True

    def __repr__(self):
        return f"Airplane(id={self.id}, current_location={self.current_location}, company={self.company})"

class Flight:
    def __init__(self, date, origin, destination, plane):
        self.date = date
        self.origin = origin  # Airport object
        self.destination = destination  # Airport object
        self.plane = plane  # Airplane object
        self.id = f"{destination.code}-{plane.company.id}-{date}"  # ID format as specified

    def take_off(self):
        # Change the location of the plane when it reaches its destination
        self.plane.current_location = self.origin

    def land(self):
        # Change the location of the plane when it reaches its destination
        self.plane.current_location = self.destination

    def __repr__(self):
        return f"Flight(id={self.id}, date={self.date}, origin={self.origin}, destination={self.destination})"

class Airport:
    def __init__(self, city):
        self.city = city  # Code of the city where the airport is located
        self.planes = []  # List of planes currently at the airport
        self.scheduled_departures = []  # List of Flight objects (departures), sorted by date
        self.scheduled_arrivals = []  # List of Flight objects (arrivals), sorted by date

    def schedule_flight(self, destination, date):
        # Finds an available airplane from an airline that serves the departure and the destination
        for plane in self.planes:
            if plane.available_on_date(date, self) and plane.company in destination.airlines:
                flight = Flight(date, self, destination, plane)
                self.scheduled_departures.append(flight)
                destination.scheduled_arrivals.append(flight)
                plane.next_flights.append(flight)
                plane.next_flights.sort(key=lambda x: x.date)  # Sort by datetime
                return flight
        return None

    def info(self, start_date, end_date):
        # Displays every scheduled flight from start_date to end_date
        print(f"Scheduled flights from {self.city} airport:")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(flight)

    def __repr__(self):
        return f"Airport(city={self.city})"

if __name__ == "__main__":
    # Create Airlines
    airline1 = Airline("AA", "Airline One")
    airline2 = Airline("BB", "Airline Two")

    # Create Airplanes
    plane1 = Airplane(1, airline1)
    plane2 = Airplane(2, airline2)

    # Create Airports
    airport1 = Airport("NYC")
    airport2 = Airport("LAX")

    # Add planes to airports
    airport1.planes = [plane1]
    airport2.planes = [plane2]

    # Schedule a flight
    flight1 = airport1.schedule_flight(airport2, "2024-07-20")
    if flight1:
        print(f"Flight scheduled: {flight1}")
    else:
        print("No available plane for the flight.")

    # Display airport info
    airport1.info("2024-07-01", "2024-07-31")
    airport2.info("2024-07-01", "2024-07-31")
