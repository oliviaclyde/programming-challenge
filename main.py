from utilities.elevator import Elevator
from control.elevatorController import ElevatorController


def main():
    
    # Call is made to an elevator
    # Elevator responds, 
    # -Needs to increment num of trips
    # -Needs to report as it moves from floor to floor
    # -Needs to report when opens/closes doors
    # Write test file for debugging
    
                    
   controller = ElevatorController(2, 5)  
   
   print("Welcome.")
   
   print(controller.floors)
   
   
   nearestElevator = ElevatorController.getNearestElevator(4)
   
   print(nearestElevator)

#    callElevator(nearestElevator, 4)

      

if __name__ == "__main__":
    main()