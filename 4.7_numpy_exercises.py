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

#Numpy extra exercises
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a= np.sum([a])
print (sum_of_a)

## Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_of_a= np.min([a])
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_of_a= np.max([a])
print(max_of_a)

## Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_of_a= np.mean([a])
print(mean_of_a)

## Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

product_of_a= np.product([a])
print(product_of_a)

## Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

squares_of_a= a**2

print(squares_of_a)
