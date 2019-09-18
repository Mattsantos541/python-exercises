#control exercises

#Conditional Basics

#1a
##prompt the user for a day of the week, print out whether the day is Monday or not

day = input("day of the week")
if day == "Monday":
    print("Monday")
else:
    print ("not Monday")
#b
###prompt the user for a day of the week, print out whether the day is Monday or not
day = input("day of the week")
if day == ("Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
    print ("Weekday")
else:
    print ("not workday")
#c 
##create variables and make up values for
hours= 40
rate= 25
if hours <= 40:
    total = hours * rate
else:
    total = 40 * rate + (hours - 40) * (1.5 * rate)

# 2. Loop Basics
# A  Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
print(i)
    i += 1

##B   Create a while loop that will count by 2's starting with 0 and ending at 100. 
#Follow each number with a new line.
n = 0
while n<= 100:
print(n)
    n +=2
##C Alter your loop to count backwards by 5's from 100 to -10.

n = 100 
while n >= -10:
print(n)
    n-=5
## D Create a while loop that starts at 2, and displays the number squared on each 
#line while the number is less than 1,000,000. Output should equal:
n = 2
while n <= 1000000:
    print (n)
    n**=2
##E
n= 100
while n >= 5:
    print (n)
    n -=5

### For Loops
#Write some code that prompts the user for a number, then shows a multiplication 
#table up through 10 for that number.

n= input("Enter a Number")
for i in range(1, 11):
   print(n,'x',i,'=',n*i)
#2- Create a for loop that uses print to create the output shown below


##C- Prompt the user for an odd number between 1 and 50. Use a loop and a break 
# statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and the 
# continue statement to output all the odd numbers between 1 and 50, except for the 
# number the user entered.

#################################odd_num= ""
while True:
    try:
        x = int(input('Enter your number: '))
    except ValueError:
        print ('That is not a number! Try again!')
    if x in [1, 2]:
        break

while True:
  try:
      number= int(input("Enter an odd number "))
  except ValueError:
    print ("Not an odd number, try again")
  for x in number:
    if x%2==1


## DThe input function can be used to prompt for input and use that input in your 
# python code. Prompt the user to enter a positive number and write a loop that 
# counts from 0 to that number. (Hints: first make sure that the value the user 
# entered is a valid number, also note that the input function returns a string, 
# so you'll need to convert this to a numeric type.)
N= int(input("Enter a number "))
if N >0:
 for x in range(N):
   print 

## E. Write a program that prompts the user for a positive integer. Next write a 
# loop that prints out the numbers from the number the user entered down to 
for i in range(0,102,2):
    print(i)

i=0    
while i<=100:
    print(i)
    i+=2



##Fizzbuzz
#One of the most common interview questions for entry-level programmers is the 
# FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic 
# looping and conditional logic skills.

##Write a program that prints the numbers from 1 to 100.

for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
#Display a table of powers.

#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.
N= int(input("enter a number "))
numbers = []
squares = []
cubes = []

start= 1

for count in range (start, N):
  numbers.append (count)
  squares.append (count**2)
  cubes.append (count**3)

print ("numbers: ",numbers)
print ("squares: ",squares)
print ("cubes  : ",cubes)


#Convert given number grades into letter grades.

##Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.
#Grade Ranges:

#A : 100 - 88
#B : 87 - 80
#C : 79 - 67
#D : 66 - 60
#F : 59 - 0
#Bonus

#Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

Grade = int(input("enter a grade ")
if 88 <= Grade <= 100:
  print ("A")
elif 80 <= Grade <= 87:
  print ("B")
elif 67 (Grade) <= 79:
  print ("C")
elif 60 <= Grade <= 66:
  print ("D")
else:
  print("F")

#Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
#Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre. """

book_list=[{'title':"Lamb",'author':"Christopher Moore",'genre':"fiction"},
{'title':"The Lean Startup",'author':"Eric Ries",'genre':"business"},{'title':"Devil in a White City",'author':"Eric Larson",'genre':"True Crime"},{'title':"Tom Sawyer",'author':"Mark Twain",'genre':"fiction"}]
for book in book_list:
    print("The book title is: "+book['title'])
    print("The book author is: "+book['author'])
    print("The book genre is: "+book['genre'])


#Exercise 6.a
genre_filter=input("Please enter a genre")
for book in book_list:
    if book['genre']==genre_filter:
        print("The book title is: "+book['title'])
        print("The book author is: "+book['author'])