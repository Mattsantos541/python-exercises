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

## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = (
    [3, 4, 5],
    [6, 7, 8]
)

np.sum(b)
np.min(b)
np.max(b)
np.product(b)
(b)


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array([
    [3, 4, 5],
    [6, 7, 8]]
)
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
    print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 
b = np.array([
    [3, 4, 5],
    [6, 7, 8]]
)
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print(min_of_b)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]]
)
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
b = np.array([
    [3, 4, 5],
    [6, 7, 8]]
)

mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]]
)
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
        
print(product_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
b = np.array([
    [3, 4, 5],
    [6, 7, 8]]
)
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
        
print(squares_of_b)