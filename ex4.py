cars = 100
space_in_a_car = 4.0 #probably an assumption of average, comfortable space for all 100 cars
drivers = 30 #assuming 1 driver per car later below
passengers = 90 #assuming not drivers
cars_not_driven = cars - drivers #assumming all drivers are driving
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available." #no extra spaces in "" necessary
print "There are only", drivers, "drivers available." #less drivers than cars
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car." #this probably rounds to nearest integer (no floating point)

#Extra Credit
# Traceback (most recent call last):
# File "ex4.py", line 8, in <module>
# average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# Reason: 'car_pool_capacity is undefined wherease 'carpool_capacity' is

# Remainder of Extra Credit:
# 1. Carpool_capacity gives '120.0' because '4.0' is given for space per car.
# 2. Floating point numbers are simply numbers with a decimal.