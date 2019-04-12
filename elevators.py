#Programming Challenge
#Elevators in a building

#Number_of_elevators = 2
#Number_of_floors = 3
floors >= 1 and <= number_of_floors


#I would first create each elevator as an object
#elevator1
#properties
#floor =
#door = open or closed
#status = occupied or not occupied (this would represent elevator moving or not moving)
#total_trips =
#floors_traveled =

#elevator2
#properties
#floor =
#door = open or closed
#status = occupied or not occupied
#total_trips =
#floors_traveled =

#Would also need to provide for scaling the number of Elevators


#I would need to create an object called controller to initiate a call button to summon the elevator
#It can't change any property of the elevators but can interact with them
#controller
def call ()
#or
#create a variable to represent the floor the call is made from call_floor
call_floor = input("Select the floor: ")

#call button is pushed on call_floor
#each elevator would need to relay what floor it is currently on
#each elevator would need to relay what status it is in
#when  call is made, each elevator would respond with its location and status
#utilize if statments to prioritize which elevator responds
#if elevator status == unoccupied and it is on the floor closest to call_floor, then elevator floor = call_floor
#need to create a variable to determine which elevator is closer to the call_floor
#if call_floor == 1 elevator_floor,
#if elevator1 is on floor 2 and elevator2 is on floor 3, and the call_floor is 1, theh the logic would be
if status == "unoccupied" and #reference logic :
    elevator_floor = call_floor #this represents the elevator moving to the call_floor
    elif floor == call_floor:
        #the unoccupied elevator responds unless the other elevator is at the call floor
else:
    #won't move to call floor
