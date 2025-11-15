###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
print('Light switch 1 ligts one lamp.')
print('Light switch 2 ligts two lamps.')
turn_on=int(input('Which light switch you want to press? (1 or 2) (0 to save) (can\'t press twice): '))

if turn_on==1:
    light_switch1= 'True'
    print('1 bulb has been turned on.')
elif turn_on==2:
    light_switch2= 'True'
    print('2 buls have been turned on.')
else:
    print('Error.')
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on+=2
print('Number of bulbs on: ',bulbs_on)