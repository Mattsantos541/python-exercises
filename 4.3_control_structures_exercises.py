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
   print(n,'x',i,'=',num*i)