class Elevator():
    def __init__(self):
        self.status = ''
        self.proximity = ''
        self.floor = 1
        self.trips = 0
        self.needsServicing = False


    def open(self):
        print("Doors opening...")
    
    def close(self):
        print("Doors closing...")

    def elevatorOccupied(self):
        pass

    def countFloor(selection):
        for i in range (1, selection+1):
            print(i + "...")

    def elevatorRunning(self):
        print("Elevator coming...")
        countFloor(selection)
    
    def numberOfTrips(self):
        self.trips += 1
        if self.trips >= 100:
            self.status = "Inactive"
            self.needsServicing = True
            print("Elevator shutdown for servicing.")

#------End Elevator class------#
