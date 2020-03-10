import numpy as np
from utilities.elevator import Elevator

class ElevatorController():
    # groundFloor = 1
    # topFloor = 5
    
    def __init__(self, numElevators, floors):
        self.floors = floors
        self.elevators = []
        for i in range(numElevators):
            self.elevators.append(Elevator())

    # Can't go above top floor or below ground floor
    # def invalidOption(self, n):
    #     if n < ElevatorController.groundFloor:
    #         print("Invalid option. Please choose another floor.")
    #     elif n > ElevatorController.topFloor:
    #         print("Invalid option. Please choose another floor.")
    #     else:
    #         print("Calling elevator...")

    # Find which elevator is closest to the called floor 
    def getNearestElevator(self, floor):
        elevatorIndex = 0
        distance = self.floors
        for index, elevator in self.elevators:
            if np.abs(elevator.floor - floor) < distance and elevator.needsServicing == False:
                elevatorIndex = index
        return self.elevators[elevatorIndex]


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


