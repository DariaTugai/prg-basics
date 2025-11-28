import math
import matplotlib.pyplot as function
x=[]
y=[]
for i in range(0,361):
    x.append(i)
for j in x:
    y.append(math.sin(j))
function.plot(x,y)
function.show()
