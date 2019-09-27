#pandas exercises

#On average, which manufacturer has the best miles per gallon?
mpg.describe()
#How many different manufacturers are there?
mpg['manufacturer'].value_counts()
#How many different models are there?
mpg['model'].value_counts()
#Do automatic or manual cars have better miles per gallon?
trans_man= mpg.groupby('trans')['hwy'].mean()
trans_auto =mpg.groupby('trans')['cty'].mean()