##DataFrames
pip install pydataset

Copy the code from the lesson to create a dataframe full of student grades.
import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})
#Create a column named passing_english that indicates whether each student has a passing grade in reading.
df['passing_english'] = df.english > 60
#Sort the english grades by the passing_english column. How are duplicates handled?
#Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['name'])
#Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by= ["passing_english", "english"])
#Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
df.sort_values(by=['name'])


# 2 Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
#How many rows and columns are there?
mpg.info()
mpg.describe()
#What are the data types of each column?
