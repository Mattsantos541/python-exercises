##pandas_series.py
#1
#A Name the variable that holds the series fruits.
fruits = series
print (fruits)
#B Run .describe() on the series to see what describe returns for a series of strings
fruits.describe()
#C Run the code necessary to produce only the unique fruit names.
pd.unique(fruits)
#D Determine how many times each value occurs in the series.
fruits.groupby(fruits).size()

#E Determine the most frequently occurring fruit name from the series.
fruits.mode()
#F Determine the least frequently occurring fruit name from the series.
fruits.value_counts().min()
#G Write the code to get the longest string from the fruits series.
fruit_names= fruits.value_counts()
fruit_names = pd.Series(fruit_names)
fruit_names.str.len().max()
#H Find the fruit(s) with 5 or more letters in the name.

more_than_5= fruits.apply(lambda x : len(x) >=5)
fruits[more_than_5]
#Capitalize all the fruit strings in the series.
fruits.str.capitalize()

#Count the letter "a" in all the fruits (use string vectorization)
def count_a(word):
    return word.count("a")

fruits.apply(count_a)

#Output the number of vowels in each and every fruit.
def count_vowels(word):
    return word.count("a" or"e" or "i" or "o" or "u")

fruits.apply(count_vowels)

#Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.


#Write the code to get only the fruits containing "berry" in the name

#Write the code to get only the fruits containing "apple" in the name

#Which fruit has the highest amount of vowels?
#2
import pandas as pd
Numbers= pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', 
                    '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', 
                    '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', 
                    '$2,791,759.67', '$769,681.94', '$452,650.23'])
type(Numbers)

#Use series operations to convert the series to a numeric data type.


#3
#What is the minimum exam score? The max, mean, median?
print(test.mean())
print (test.max())
print (test.min())
print (test.median())
#Plot a histogram of the scores.
plt.hist(test)
plt.show()
#Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

#Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
