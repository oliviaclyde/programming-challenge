import numpy as np
from time import sleep
from utilities.elevator import Elevator

class ElevatorController():

    def __init__(self, numElevators, floors, groundFloor=1):
        self.floors = floors
        self.groundFloor = groundFloor
        self.elevators = []
        self.unprocessedCalls = []
        self.call = []
        for i in range(numElevators):
            self.elevators.append(Elevator())
        

    def invalidOption(self, selection):
        if type(selection) is not int:
            return False
        elif selection < self.groundFloor:
            return False
        elif selection > self.floors:
            return False
        else:
            return True


    def getNearestElevator(self, call):
        origin, destination = call
        elevatorIndex = 0
        distance = self.floors
        direction = 1
        if origin > destination:
            direction = -1
        else:
            direction = 1

        for index, elevator in enumerate(self.elevators):
            if (np.abs(elevator.floor - origin) < distance 
                # and np.abs(elevator.floor - origin) < elevatorIndex 
                and elevator.needsServicing == False
                and elevator.status is not "occupied"
                and elevator.getDirection() == direction
                and (
                    (elevator.floor > origin and direction < 0) 
                    or (elevator.floor < origin and direction > 0))):
                elevatorIndex = index
                distance = np.abs(elevator.floor - origin)
        print(elevatorIndex)
        return self.elevators[elevatorIndex]

    # - return nearest elevator that is moving to destination or not moving
    # Need to get direction appended to Elevator object
    # Need to append the destination floor to the elevator that is responding to the call self.floor.append(destination) - this is the floor it ends up on

    def start(self):
        while True:
            print(self.call)
            
            currentCall = self.call
            self.call = []
            for call in self.unprocessedCalls:
                pass
                # self.processCall(call)
                # self.moveAllElevators(nearestElevator)

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
            # controller needs to spit new calls into unprocessed queue
            self.unprocessedCalls.append(self.call)
    
        
    def processCall(self, call):
        nearestElevator = self.getNearestElevator(call)
        pass
        
        # originFloor, destinationFloor = UnprocessedCalls.pop(0)
        # elevator = getNearestElevator(originFloor, destinationFloor)
        # elevator.destinations.push(destination)
        # elevator.destinations.push(origin)
        # elevator.sortDestinations() # this will need to take if current floor > or < destionations


    def moveAllElevators(self, nearestElevator):
        pass 
        self.elevatorRunning()
        self.countFloor
        self.open()
        self.close()
        self.numberOfTrips()
        self.floor 


        # figure out if elevator needs to move up or down floor
        # move elevator (floor +=1 or floor -= 1)

        # elevatorDirection
        # nearestElevator.floor
        
        


#----End ElevatorController class----#



'''

Main
- Listens for calls
- *Debug exiting program 
- *Debug if invalid character is entered 

Elevator
- no logic, just properties
- destinations
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
            open doors/closedoors/etc - 
                self.elevatorRunning(floor)
                Self.open()
                self.close()
                self.elevatorOccupied();
            increment trips - self.numberOfTrips()
        increment floors elevator.countFloor()
        other crap
        Update elevator.status == "Occupied"
        Update elevator.numberOfTrips()  
        Update elevators position - elevator.floor = destination floor


def ProcessCall(self):
    originFloor, destinationFloor = UnprocessedCalls.pop(0)
    elevator = getNearestElevator(originFloor, destinationFloor)
    elevator.destinations.push(destination)
    elevator.destinations.push(origin)
    elevator.sortDestinations() # this will need to take if current floor > or < destionations

'''