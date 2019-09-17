##Command Line Checkbook Application

##Greet on opening
name= input( "Welcome, may i get your name? ")
print('Hello ' + str(name))
print('\n                                   ')
print ("What can I do for you today? ")
print('\n')
options= ([
    "1. Balance",
    "2. Deposit",
    "3. Withdrawl",
    "4. End Session"
  ])
while True:
  choice = input("1. Balance 2. Deposit 3. Withdrawl 4. End Session. [1/2/3/4]")
