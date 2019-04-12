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
#status = occupied or unoccupied (this would represent elevator moving or not moving)
#total_trips =
#floors_traveled =

#elevator2
#properties
#floor =
#door = open or closed
#status = occupied or unoccupied
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
#if call_floor == elevator_floor and elevator_status == unoccupied, elevator1 = call_floor
if elevator_status == occupied:
    if elevator1_floor > call_floor or elevator1_floor < call_floor:
        #elevator will not respond to the call
        #total_trips will not increment
        #floors traveled will not increment
        #the other elevator will respond
elevator2_floor = call_floor #this represents the elevator moving to the call_floor
#This logic will need to be improved to scale for more than 2 elevators in alternate scenarios
if status == "unoccupied" and elevator_floor == call_floor:
    total_trips += 1 #increment total_trips
    floors_traveled += 1 #increment floors_traveled
#the occupied elevator responds if it is at the call floor
if status == "occupied" and evelator_floor == call_floor:
    total_trips += 1 #increment total_trips
    floors_traveled += 1 #increment floors_traveled
