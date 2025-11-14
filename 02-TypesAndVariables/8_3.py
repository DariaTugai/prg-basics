###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

tc=float(input('Enter t in Celsius: ')) # t in Celsius from keyboard
tk= tc+273.15 # t converted to Kelvin
tf= tc*9/5 +32 # t converted to Farenheit
print(f'{tc} Celsius degrees equals to {tk} Kelvin degrees and to {tf} Farenheit degrees.')