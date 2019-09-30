import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from pydataset import data


#1 What does the distribution of petal lengths look like?

sns.distplot(iris.petal_length)

#2 s there a correlation between petal length and petal width?
sns.relplot(data=iris, x='petal_length', y='petal_width')

#3#3Would it be reasonable to predict species based on sepal width and sepal length?
sns.jointplot(data=iris, x='petal_length', y='petal_width')



#anscombe  1-Using the lesson as an example, use seaborn's load_dataset function to load the anscombe 
#data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?
anscombe.groupby('dataset').describe()

sns.relplot(x='x', y='y', data=anscombe)

##Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the effectiveness of the different insect sprays.
sns.boxplot(data=IS, x='count', y='spray')



#Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions

swiss.describe()
is_catholic= swiss['Catholic']
#Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic
is_catholic= swiss['Catholic']
is_catholic >50

#Does whether or not a province is Catholic influence fertility?
sns.relplot(x='Catholic', y='Fertility', data=swiss).set_title('Fertility vs being Catholic')

#What measure correlates most strongly with fertility?


