###mathplotlib exercises
import matplotlib.pyplot as plt
print(plt)
#Use matplotlib to plot the following equation: y = x **2 -x +2
x= list(range(140))
y = [x**2-x +2 for x in x]
plt.plot(x, y)
plt.title("x **2 -x +2")


plt.show()


#Add an anotation for the point 0, 0, the origin.


######

#Create and label 4 separate charts for the following equations (choose a range for x that makes sense):
#square root
import matplotlib.pyplot as plt
import math
#y= sqrt(x)

x= list(range(50))
y = [math.sqrt(x) for x in x]
plt.plot(x, y)
plt.show()

#x**3
import matplotlib.pyplot as plt
x= list(range(20))
y = [x**3 for x in x]
plt.plot(x, y)
plt.xscale("linear")
plt.yscale("linear")
plt.show()

#tan(x)
import matplotlib.pyplot as plt
import math
x= list(range(50))
y= [math.tan(x)for x in x]

plt.plot(x,y)
plt.xscale("linear")
plt.yscale("linear")
plt.show

#2 **x
import matplotlib.pyplot as plt

x= list(range(20))
y = [2**x for x in x]
plt.xscale("linear")
plt.yscale("linear")
plt.plot(x, y)

plt.title("x **2 -x +2")
###
#Combine the figures you created in the last step into one large figure with 4 subplots.
import matplotlib.pyplot as plt

# Data for plotting
x1= list(range(20))
y1 = [x**3 for x in x1]
x2= list(range(1, 1000))
y2= [math.tan(x)for x in x2]
x3= list(range(20))
y3= [2**x for x in x3]
x4= list(range(50))
y4 = [math.sqrt(x) for x in x4]

plt.subplots(1,2)
plt.plot(x1, y1)
plt.title(("Cubed"))

plt.subplots(1,2)
plt.plot(x2, y2)
plt.title("Tan")

plt.subplots(1,2)
plt.plot(x3, y3)
plt.title("log")

plt.subplots(1,2)
plt.plot(x4, y4)
plt.title("quadratic")

plt.show()



#Combine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points. Be sure to include a legend.


