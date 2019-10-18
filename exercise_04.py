cars= 100
space_in_a_car = 4.0
driver = 30
passengger = 90
cars_not_driver = cars - driver
cars_driver = driver

carpool_capacity = cars_driver * space_in_a_car
average_passenger_per_car = passengger / cars_driver

print("There are", cars, " car available.")
print("There are only", driver," driver available.")
print("There will be", cars_not_driver, "empty cars today")
print("We can transport", carpool_capacity,  " people today")
print("We have", passengger, " to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")