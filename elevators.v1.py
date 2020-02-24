
def main():

       # test = ElevatorController().invalidOption
    # print(test(selection))

    class ElevatorController():
        floors = 5
        numElevators = 2
        groundFloor = 1
        topFloor = 5
        
        def __init__(self, floor):
            self.floor = floor

        def nearestElevator():
            pass

         # Can't go above top floor or below ground floor
        def invalidOption(self, n):
            if n < ElevatorController.groundFloor:
                print("Invalid option. Please choose another floor.")
            elif n > ElevatorController.topFloor:
                print("Invalid option. Please choose another floor.")
            else:
                print("Calling elevator...")

    
    selection = int(input("Welcome. Please select a floor:   "))
    controller = ElevatorController(selection)
    print(controller.invalidOption(selection))


#----End ElevatorController class----#


    class Elevator():

        def __init__(self, status, floor, trips, needsServicing):
            self.status = status
            self.floor = floor
            self.trips = trips
            self.needsServicing = needsServicing

        def open(self):
            print("Doors opening...")
        
        def close(self):
            print("Doors closing...")

        def callElevator(self, floor, direction):
            pass

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

                    
    elevator1 = Elevator("Unoccupied", 1, 0, False)
    elevator2 = Elevator("Unoccupied", 2, 0, False)


    print(elevator1.status)
    print(elevator2.floor)

#----End Elevator class----#


if __name__ == "__main__":
    main()