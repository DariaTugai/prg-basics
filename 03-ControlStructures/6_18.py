coordinates=input('Enter coordinates (x,y): ')
x=int(coordinates[1])
y=int(coordinates[3])
if x>0 and y>0:
    print(f'Point P{coordinates} is in the first quadrant of the coordinate system')
elif x<0 and y>0:
    print(f'Point P{coordinates} is in the second quadrant of the coordinate system')
elif x<0 and y<0:
    print(f'Point P{coordinates} is in the third quadrant of the coordinate system')
elif x>0 and y<0:
    print(f'Point P{coordinates} is in the fourth quadrant of the coordinate system')
elif x==0 or y==0:
    print(f'Point P{coordinates} is in on the grid lines of the coordinate system')
