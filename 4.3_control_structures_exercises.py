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