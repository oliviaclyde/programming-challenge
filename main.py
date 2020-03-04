from utilities import elevator
from utilities import elevatorController


def main():
    
    # Call is made to an elevator
    # Elevator responds, 
    # -Needs to increment num of trips
    # -Needs to report as it moves from floor to floor
    # -Needs to report when opens/closes doors

    
                    
    elevator1 = elevator.Elevator("unoccupied", "not called", 4, 0, False)
    elevator2 = elevator.Elevator("unoccupied", "not called", 2, 0, False)


    print(elevator1.status)
    print(elevator2.floor)


      
    selection = int(input("Welcome. Please select a floor:   "))
    controller = elevatorController.ElevatorController(selection)
    print(controller.invalidOption(selection))
    print(controller.nearestElevator(selection))



if __name__ == "__main__":
    main()