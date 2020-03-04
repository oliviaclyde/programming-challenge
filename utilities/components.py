import numpy as np

class Elevator():
    def __init__(self, status, proximity, floor, trips, needsServicing):
        self.status = status
        self.proximity = proximity
        self.floor = floor
        self.trips = trips
        self.needsServicing = needsServicing

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

class ElevatorController():
    floors = 5
    numElevators = 2
    groundFloor = 1
    topFloor = 5
    
    def __init__(self, floor):
        self.floor = floor

        # Can't go above top floor or below ground floor
    def invalidOption(self, n):
        if n < ElevatorController.groundFloor:
            print("Invalid option. Please choose another floor.")
        elif n > ElevatorController.topFloor:
            print("Invalid option. Please choose another floor.")
        else:
            print("Calling elevator...")

    # Find which elevator is closest to the called floor 
    def nearestElevator(self, selection):
        floorOptions = []
        floorOptions.append(elevator1.floor)
        floorOptions.append(elevator2.floor)
        floorOptions = np.asarray(floorOptions)
        closestFloor = (np.abs(floorOptions - selection)).argmin()
        if floorOptions[closestFloor] == elevator1.floor:
            print("Elevator 1 responding.") 
            elevator1.proximity == "closest"
        else:
            print("Elevator 2 responding.")
            elevator2.proximity == "closest"
        return floorOptions[closestFloor]
        
        # Debug why elevator proximity when printed isn't updating 
        # print(elevator1.proximity)

    def callElevator(selection):
        pass 
        # Closest elevator has already been determined
        # if elevator1.status == "unoccupied" & elevator1.proximity == "closest"
        # Elevator responds by counting floors to the called floor 
        # Doors open
        # Adjust reponding elevator's status - elevator.status == "Occupied"
        # Adjust trip count of responding elevator - elevator.numofTrips() 
        # Adjust new resting position of responding elevator's floor - elevator.floor == selection

    def selectFloor():
        pass
        # After the elevator has been called, this function will be used to 
        # Detemine where the passenger wants to go 
        # A destination floor will be selected
        # Doors close
        # Count floors while traveling 
        # Doors open
        # Update elevator.status to "unoccupied" 
        # Update elevator.proximity to "not  called"
        # Update elevator.trips to increment += 1 
        # Adjust new resting position of responding elevator - elevator.floor = selection

#----End ElevatorController class----#