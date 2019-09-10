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


#1 You have rented some movies for your kids: The 
# little mermaid (for 3 days), Brother Bear (for 
# 5 days, they love it), and Hercules (1 day, you don't 
# know yet if they're going to like it). If price for a 
# movie per day is 3 dollars, how much will you have to pay?

Movies= [

{"Movie":"Little Mermaid", "Rental": 3, "preference":"Do no know if they like it"},
{"Movie":"Brother Bear", "Rental": 5, "preference":"Kids Love it"},
{"Movie":"Herceules", "Rental": 1, "preference":"Do not know if they like it"}
]

##If price for a movie per day is 3 dollars, 
# how much will you have to pay?
Total_Spent= 0  
for x in Movies: 
    Total_Spent = x["Rental"] * 3
