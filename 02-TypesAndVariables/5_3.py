###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a= '))
b = int(input('b= '))
h = int(input('h= '))
volume=a*b*h
surface=2*b*h+2*b*a+2*h*a
print(f'The volume is {volume} and the surface area is {surface}')