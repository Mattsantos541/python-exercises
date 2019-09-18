##Assessment

## 1isnegative
def isnegative(x):
    if (x<0):
        return True
    else:
        False
   

    assert isnegative(-2) == True

print("it works")


## 2 CountEvens
def countevens(numbers):
    count = 0
    for x in numbers:
        if x % 2 == 0:
            count += 1
    return count
       
    assert countevens([1, 2, 3]) == 1
    assert countevens([2, 5, 6]) == 2
print("it works")


##3 increment_odds
def increment_odds(numbers):
    L= []
    for x in numbers:
        if x %2 ==1:
            L.append(x)
            return L

    assert([1, 2, 3])== [1, 3]
    assert(1, 3, 4, 5, 9)== [1, 3, 5, 9]
print("It Works")

##4 average
def average(numbers):
    return sum(numbers)/len(numbers)

    assert([1, 2, 3])== 2
    assert([4, 6, 8, 10, 12])== 9
print ("it works")


##5 name_to_dict
def name_to_dict(names):
    Fullname= {}
    for x in names:
      first_name= x.split()
      first_name = x.strip().split(' ')[0]
      last_name = ' '.join((x + ' ').split(' ')[1:]).strip()
      
      return Fullname
    
    assert name_to_dict('Ada Lovelace') == {'first_name': 'Ada', 'last_name': 'Lovelace'}
    print("it works")


##capitalize_names
def capitalize_names(name):
  
##7 Countvowels
def Countvowels(words):
    count= 0
    for x in word:
        if [x=="a", x=="e", x=="i", x=="o", x=="u", x=="A", x=="E", x=="I", x=="O", x=="U"]:
            count += 1
            return count>0
    assert Countvowels("dddd")== 0
    assert Countvowels("codeup")== 3
print("it works")

##8 analyze_word
