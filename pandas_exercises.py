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


#2 Joining and Merging

#Copy the users and roles dataframes from the examples above. What do you think a right join would look like? An outer join? What happens if you drop the foreign keys from the dataframes and try to merge them?
#users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})

users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')
#3 Getting data from SQL databases