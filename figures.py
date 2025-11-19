def draw_square(length):
    for i in range(length):
        if i== 0 or i==length-1:
            print ('*'*length)
        else:
            print("*"+" "*(length -2)+'*')
       
print(draw_square(6))