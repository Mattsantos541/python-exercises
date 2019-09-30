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




