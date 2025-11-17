car_speed=int(input('Enter car speed (in km/h): '))
speed_limit_min=40
speed_limit_max=140
if car_speed<40 or car_speed>140:
    print('Warning: invalid car speed!!')
else:
    print('It\'s ok!!')