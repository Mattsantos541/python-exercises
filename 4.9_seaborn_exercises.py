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
plt.figure(figsize=(7,7))
sns.heatmap(swiss.corr(),
            vmin=-1,
            cmap='coolwarm',
            annot=True);
#Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.
chipotle['price'] = chipotle['item_price'].apply(lambda x: float(x[1:]))
revenues = chipotle.groupby('item_name')['price'].sum().sort_values()

top_revenues = pd.Series(revenues.tail(4))

to_bar = pd.DataFrame()
to_bar['item'] = top_revenues.index
to_bar['revenue'] = top_revenues.values
sns.barplot(x='item', y='revenue', data=to_bar)
#Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant 
#line showing the average change in reaction time.
sleep= date('sleepstudy')
sns.lineplot(x="Days", y="Reaction", data=sleepstudy)
sleep
sns.set_style('dark')
sns.set_context(font_scale=1,rc={"grid.linewidth": .5, "axes.linewidth": .5, "ytick.major.width": .5, "xtick.major.width": .5,"lines.linewidth": 0.5})
palette = sns.color_palette("husl", 18)
sns.lineplot(x='Days', y='Reaction', hue='Subject', data=sleep, palette=palette)
sns.set_context(rc={"lines.linewidth": 2})
sns.lineplot(x='Days', y='Reaction', data=sleep, ci=None)
# sns.despine()
plt.show()
import pandas as pd
data= pd.read_csv('Social_Network_Ads.csv')