#this assigns 100 to the var cars
cars = 100

#this assigns 4.0 to the var space_in_a_car
space_in_a_car = 4.0

#this assigns 30 to the var drivers
drivers = 30

#this assigns 90 to the var passengers
passengers = 90


cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#extra credit
print "Extra Credit: the variable name was mis typed on line 8. The variable from line 7 does not have a space, it shoudnt have one when called in line 8"

