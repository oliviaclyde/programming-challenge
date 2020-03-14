from utilities.elevator import Elevator
from control.elevatorController import ElevatorController


def main():
   
    numElevators = int(input("Enter how many elevators are in your building...  "))
    floors = int(input("Enter how many floors are in your building...  "))        
    
    controller = ElevatorController(numElevators, floors)  

    print("Welcome.")
    selection = int(input("Please select a floor:  "))
    controller.invalidOption(selection)

    # while True:
    #     try:
    #         selection = int(input("Please select a floor:  "))
    #         break
    #     except ValueError:
    #         print("The input was not a valid integer.")
   
    #nearestElevator = controller.getNearestElevator(4)
   
    #print(nearestElevator)
    
      

if __name__ == "__main__":
    main()