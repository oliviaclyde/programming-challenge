# Call is made to an elevator
    # Elevator responds, 
    # -Needs to increment num of trips
    # -Needs to report as it moves from floor to floor
    # -Needs to report when opens/closes doors
    # Write test file for debugging



import numpy as np
from utilities.elevator import Elevator

class ElevatorController():

    def __init__(self, numElevators, floors, groundFloor=1):
        self.floors = floors
        self.groundFloor = groundFloor
        self.elevators = []
        for i in range(numElevators):
            self.elevators.append(Elevator())


    # Can't go above top floor or below ground floor
    def invalidOption(self, selection):
        if type(selection) is not int:
            print("Invalid option. Please choose another floor.")
            return False
        elif selection < self.groundFloor:
            print("Invalid option. Please choose another floor.")
            return False
        elif selection > self.floors:
            print("Invalid option. Please choose another floor.")
            return False
        else:
            print("Calling elevator...")
            return True

    # Find which elevator is closest to the called floor 
    def getNearestElevator(self, floor):
        elevatorIndex = 0
        distance = self.floors
        for index, elevator in enumerate(self.elevators):
            if np.abs(elevator.floor - floor) < distance and elevator.needsServicing == False:
                elevatorIndex = index
        return self.elevators[elevatorIndex]

    def goUp(self):
        pass
        # Call nearestElevator
        # selectFloor()
        

    def goDown(self):
        pass
        # Call nearestElevator
        # selectFloor()
       
        

    def callElevator(self, nearestElevator, selection):
        pass 
        # if Elevator1.status == "unoccupied" & elevator1.proximity == "closest"
        # Elevator responds by counting floors to the called floor 
        elevator.open()
        # Adjust reponding elevator's status - elevator.status == "Occupied"
        # Adjust trip count of responding elevator - elevator.numofTrips() 
        # Adjust new resting position of responding elevator's floor - elevator.floor == selection

    def selectFloor():
        pass
        # After the elevator has been called, this function will be used to 
        # Detemine where the passenger wants to go 
        # A destination floor will be selected
        # Elevator.close()
        # Elevator.countFloors() # Count floors while traveling 
        # Doors open
        # Update elevator.status to "unoccupied" 
        # Update elevator.proximity to "not  called"
        # Update elevator.trips to increment += 1 
        # Adjust new resting position of responding elevator - elevator.floor = selection

#----End ElevatorController class----#


