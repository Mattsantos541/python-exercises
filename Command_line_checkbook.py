##Command Line Checkbook Application

##Greet on opening
name= input( "Welcome, may i get your name? ")
print('Hello ' + str(name) +' What can I do for you? ' )
def checking_options():
  print ("What can I do for you today? ")
  print([
    "1. Balance",
    "2. Deposit",
    "3. Withdrawl",
    "4. End Session"
  ])

checking_options()