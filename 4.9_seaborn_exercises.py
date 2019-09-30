import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from pydataset import data


#1 What does the distribution of petal lengths look like?

sns.distplot(iris.petal_length)

#2 s there a correlation between petal length and petal width?
sns.relplot(data=iris, x='petal_length', y='petal_width')