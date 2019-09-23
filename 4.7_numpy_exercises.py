##Numpy
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#count negative numbers
a[a<0]

#count postive numbers
a[a>0]

#How many even positive numbers are there?
a.logical_and([a>0 and a%2==0])

#If you were to add 3 to each data point, how many positive numbers would there be?
a1 = (a+3)
a2 = a1 ([a1 >0])

#If you squared each number, what would the new mean and standard deviation be?
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a1= a**2
print(a1)
print(a1.mean())
print(a1.std())


#A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a - (a.mean())

#Calculate the z-score for each data point. Recall that the z-score is given by:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a1 - (a.mean())
AZ= a1- (a.std())
print (AZ)