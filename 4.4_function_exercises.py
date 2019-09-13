##Function Exercises

"""Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise."""
def is_two(n):
  for a in n:
    if type(a) == int or type(a) == float:
      True
    else:
      False
assert is_two(2)
assert is_two(3)


##Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
  for l in letter:
    if l in["a", "e", "i", "o","u", "A", "E", "I", "O", "U"]:
      return True
    else:
      return False 

## 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this
def is_consonant(letter):
  for l in letter:
    if l in["a", "e", "i", "o","u", "A", "E", "I", "O", "U"]:
      return False
      print("Is a consonant")
    else:
      print("is a vowel")

print (is_consonant("b")) 


## 4   Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def Capital(word):
  letter= word.split()
  for n in letter:
    if n[0] in ['a','e','i','o','u','A','E','I','O','U']:
      return False
    else:
      print(word.capitalize)
      print(Capital())

    print(Captial("Apple"))
    print(Capital("Mango"))
##5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(check_amount, tip):
    tip_amount = total_bill * (tip_percent/100)
    return tip_amount

#Input amount
total_bill = (float(input("What was the total of your bill with tax?")))
tip_percent = (float(input("How much would you like to tip? (0-1)"))) 

tip_amount= (tip_percent * total_bill)
print(total_bill + tip_amount)

##6 Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount):
  discount_amount = (original_price * discount)
  return discount_amount

final_price = (original_price - discount_amount)

print(final_price)

##7Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(number):
  for x in number:
    x.remove(",")
    return number
    print(number)
##Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F)
def get_letter_grade(test):
    if 88 <= test <= 100:
      print ("A")
    elif 80 <= test <= 87:
      print ("B")
    elif 67 <= test <= 79:
      print ("C")
    elif 60 <= test <= 66:
      print ("D")
    else:
      print("F")

##9Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(L):
    letter=[]
    for x in L:
        if x=="aeiouAEIOU":
            L.remove(x)
            return L
            print (L)

##10Define a function named normalize_name. It should accept a string and return a valid python identifier, that is: