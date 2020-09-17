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


    endProgram = None


    print("At any time create a call by entering origin and destination. (Ex. 1,3) To quit, type Y")
    while endProgram is not "y" or "Y":
        selection = input()
        splitSelection = selection.split(',')
        origin = int(splitSelection[0])
        destination = int(splitSelection[1]) 
        controller.newCall(origin, destination)
        #controller.elevatorResponding(destination)

   
#  Need a way to exit
# Need to debug if a character , or = is hit in error. Throws and error in the program
   
if __name__ == "__main__":
    main()