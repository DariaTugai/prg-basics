###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    num=1
    for line in file:
        print(num,'. ',line, end="")
        num+=1