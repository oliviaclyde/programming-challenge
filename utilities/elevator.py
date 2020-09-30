class Elevator():
    def __init__(self, id):
        self.status = ''
        self.proximity = ''
        self.floor = 1
        self.trips = 0
        self.needsServicing = False
        self.destinations = []
        self.id = id

    def getDirection(self):
        if len(self.destinations) == 0:
            return 0
        elif self.destinations[0] < self.floor:
            return -1
        else: 
            return 1  
    
    def addDestination(self, destination):
        self.destinations.append(destination)
        # self.destinations.sort()
    

    def open(self):
        print("Doors opening...")
    
    def close(self):
        print("Doors closing...")

    def elevatorOccupied(self):
        setattr(Elevator, self.status, 'occupied')
    
    def elevatorUnoccupied(self):
        setattr(Elevator, self.status, '')

    def move(self):
        self.floor += self.getDirection()
        print(f"Elevator {self.id}: moving to {self.floor}.")
        

    def report(self):
        if len(self.destinations) > 0 and self.floor == self.destinations[0]:
            self.destinations.pop(0)
            # self.elevatorOccupied()
            self.open()
            self.close()
            self.numberOfTrips() 

    def numberOfTrips(self):
        self.trips += 1
        if self.trips >= 100:
            setattr(Elevator, self.status, 'Inactive')
            setattr(Elevator, self.needsServicing, 'True')
            print("Elevator shutdown for servicing.")

#------End Elevator class------#
