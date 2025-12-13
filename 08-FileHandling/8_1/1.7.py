###
# Reads the entire contents of a file
#
file_car = open('08-FileHandling/car_park.txt').read().split('\n')
tot_cars = 0
for num in file_car:
    tot_cars+=int(num)
print(tot_cars)