from utilities.elevator import Elevator
from control.elevatorController import ElevatorController
from threading import Thread

def startController(controller):
    controller.start()
    


def main():
   
    numElevators = int(input("Enter how many elevators are in your building...  "))
    floors = int(input("Enter how many floors are in your building...  "))        
    
    controller = ElevatorController(numElevators, floors)  

    
    
    controllerThread = Thread(target=startController, args=(controller,))
    
    controllerThread.start()


    print("At any time create a call by entering origin and destination. (Ex. 1,3) To quit, type Y")
    while True:
        selection = input()
        if selection == "y" or selection == "Y":
            controller.end()
            break
        splitSelection = selection.split(',')
        origin = int(splitSelection[0])
        destination = int(splitSelection[1]) 
        controller.newCall(origin, destination)
       


   
if __name__ == "__main__":
    main()