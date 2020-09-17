# Call is made to an elevator
    # Elevator responds, 
    # -Needs to increment num of trips
    # -Needs to report as it moves from floor to floor
    # -Needs to report when opens/closes doors
    # Write test file for debugging



import numpy as np
from time import sleep
from utilities.elevator import Elevator

class ElevatorController():

    def __init__(self, numElevators, floors, groundFloor=1):
        self.floors = floors
        self.groundFloor = groundFloor
        self.elevators = []
        self.call = []
        for i in range(numElevators):
            self.elevators.append(Elevator())


    # Can't go above top floor or below ground floor
    def invalidOption(self, selection):
        if type(selection) is not int:
            return False
        elif selection < self.groundFloor:
            return False
        elif selection > self.floors:
            return False
        else:
            return True

    # Find which elevator is closest to the called floor 
    def getNearestElevator(self, call):
        origin, destination = call
        elevatorIndex = 0
        distance = self.floors
        direction = None
        if origin > destination:
            direction = -1
        else:
            direction = 1

        for index, elevator in enumerate(self.elevators):
            if np.abs(elevator.floor - origin) < distance 
                and np.abs(elevator.floor - origin) < elevatorIndex 
                and elevator.needsServicing == False
                and elevator.getDirection() == direction
                and (
                    (elevator.floor > origin and direction < 0) 
                    or (elevator.floor < origin and direction > 0) ):
                elevatorIndex = index
        
        print(elevatorIndex)
        return self.elevators[elevatorIndex]

    def start(self):
        while True:
            print(self.call)
            
            currentCall = self.call
            self.call = []
            # Check for call
            # Process call -> call the elevators
            # ELevator will move the floor 
            sleep(2)
            

    def newCall(self, origin, destination):
        if self.invalidOption(origin) == False or self.invalidOption(destination) == False or origin == destination:
            print("Invalid selection.")
        else:
            print("Processing call...")
            self.call = [origin, destination]
            self.elevatorResponding()

    
    
    
    
    def elevatorResponding(self):
        nearestElevator = self.getNearestElevator()
        moveElevator(nearestElevator)

    def moveElevator(self, nearestElevator):
        # figure out if elevator needs to move up or down floor
        # move elevator (floor +=1 or floor -= 1)

        elevatorDirection
        nearestElevator.floor
        
        # elevator.elevatorRunning()
        # elevator.countFloor()
        # elevator.open()
        # if Elevator1.status == "unoccupied" & elevator1.proximity == "closest"
        # Elevator responds by counting floors to the called floor 
        # Adjust reponding elevator's status - elevator.status == "Occupied"
        # Adjust trip count of responding elevator - elevator.numofTrips() 
        # Adjust new resting position of responding elevator's floor - elevator.floor == selection


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



'''

Main
- Listens for calls

Elevator
- no logic, just properties
- desitinations
- getDirection()
    return 1 or -1 determine if destination > or < self.floor

Controller
property unprocessedCalls[]

- NewCall(call)
    - Add new call to UnprocessedCalls[]

- Start() #loop ever 2 sec
    for call in self.unprocesedCalls()
        self.ProcessCall(call)
        self.MoveAllElevators()

def: GetNearestElevator(originFloor, destination)
    - return nearest elevator that is moving to destination or not moving

def MoveAllElevators:
    for elevator in self.elevators
        if floor > < then move + or - 1
            move 1 floor
        if floor = destination[0]
            pop the dest
            open doors/closedoors/etc
            increment trips
        increment floors
        other crap

def ProcessCall(self):
    originFloor, destinationFloor = UnprocessedCalls.pop(0)
    elevator = getNearestElevator(originFloor, destinationFloor)
    elevator.destinations.push(destination)
    elevator.destinations.push(origin)
    elevator.sortDestinations() # this will need to take if current floor > or < destionations

'''