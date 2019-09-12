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
