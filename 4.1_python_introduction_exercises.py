##first exercises

print ("Hello World")
greetings= "How are you?"
print (greetings)
####this is working


###first exercises
type(99.9)
type("False")
type(False)
type('0')
type(0)
type(True)
type('True')
type([{}])
type({'a': []})

A term or phrase typed into a search box? string
If a user is logged in? bool
A discount amount to apply to a user's shopping cart? float
Whether or not a coupon code is valid? bool
An email address typed into a registration form? tuple
The price of a product? float
A Matrix? dict
The email addresses collected from a registration form? tuple
Information about applicants to Codeup's data science program? str

##For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

'1' + 2= Error
6 % 4= 2
type(6 % 4)= int
type(type(6 % 4))= type
'3 + 4 is ' + 3 + 4= error
0 < 0= False
'False' == False= False
True == 'True'= False
5 >= -5= True
!False or False
True or "42"
!True && !False
6 % 5 = 1
5 < 4 and 1 == 1 = False
'codeup' == 'codeup' and 'codeup' == 'Codeup'= False
4 >= 0 and 1 !== '1'= Error
6 % 3 == 0 True
5 % 2 != 0 True
[1] + 2= Error
[1] + [2]= [1, 2]
[1] * 2= [1, 1]
[1] * [2]= error
[] + [] == []= True
{} + {}= error

#########No need for lists
#1 You have rented some movies for your kids: The 
# little mermaid (for 3 days), Brother Bear (for 
# 5 days, they love it), and Hercules (1 day, you don't 
# know yet if they're going to like it). If price for a 
# movie per day is 3 dollars, how much will you have to pay?
#####No need for lists
little_mermaid= 3 
Brother_Bear= 5
Hercules= 1

Total_rental= (little_mermaid + Brother_Bear + Hercules) *3
print (Total_rental)
#########If price for a movie per day is 3 dollars, 
# how much will you have to pay?

####Suppose you're working as a contractor for 3 companies: Google, Amazon and 
# Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, 
# Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

FB = 350
A = 380
Goog = 400

Salary = (FB *10)+(A *4)+(Goog * 6)

print (Salary)

###A student can be enrolled to a class only if the class is not full and the class 
# schedule does not conflict with her current schedule.
Students = ("not")
schedule = ("open")

if Students == ("not") and schedule == ("open"):
  print ("can sign up for class")
else:
  print ("not available")


###A product offer can be applied only if people buys more than 2 items, and the 
# offer has not expired. Premium members do not need to buy a specific amount of products.

purchase= 1
offer= "active"
premium = "no"
if premium == "yes" and offer== "active":
  print ("Offer is valid")
elif purchase > 2 and offer == "active":
  print ("offer is valid")
else:
  print ("offer is no good")

username = 'codeup'
password = 'notastrongpassword'

##the password must be at least 5 characters

password_greater_5 = len(username) >=5

##the username must be no more than 20 characters

len(password)<= 20

##the password must not be the same as the username

username != password

##neither can have white space

