class Elevator():
    def __init__(self):
        self.status = ''
        self.proximity = ''
        self.floor = 1
        self.trips = 0
        self.needsServicing = False
        self.destinations = []


    def getDirection(self):
        if destination > self.floor:
            return 1
        else: 
            return -1  

    def open(self):
        print("Doors opening...")
    
    def close(self):
        print("Doors closing...")

    def elevatorOccupied(self):
        setattr(Elevator, self.status, 'occupied')

    def countFloor(floor):
        for i in range (1, (floor+1)):
            print(i + "...")

    def elevatorRunning(self):
        print("Elevator coming...")
        return countFloor(floor)
    
    def numberOfTrips(self):
        self.trips += 1
        if self.trips >= 100:
            setattr(Elevator, self.status, 'Inactive')
            setattr(Elevator, self.needsServicing, 'True')
            print("Elevator shutdown for servicing.")

#------End Elevator class------#
