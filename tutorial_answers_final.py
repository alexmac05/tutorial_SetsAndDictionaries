# Question 1:
# Exercise 1: Make sure python is loaded and working
# Uncomment the below code and run it
#import sys
#print(sys.version_info)
#print(sys.version)
#print("Hello world!")

#######################################################################################################################
# Exercise 2: Get rid of all of the duplicates in this list.
# Think about the complexity of your solution. 
#(You'll find it is O(n^2), can you explain why as an exercise?)

#myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']


# Answer Question 2
#newList = []
#for i in myList:
#    if i not in newList:
#        newList.append(i)

#print(newList)


#RESOURCES
# Complexity cheetsheet http://bigocheatsheet.com/
# Cool link https://www.peterbe.com/plog/uniqifiers-benchmark
# https://wiki.python.org/moin/TimeComplexity

#######################################################################################################################
#A PAUSE HERE FOR TIMEIT

#An example
#import timeit
#timeit.timeit('char in text', setup='text = "sample string"; char = "g"')


#An example using the Timer class and methods
#import timeit
#foo = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
#foo.timeit()

#A multi-line example
#setup='import string'

#myStatement = '''
#myList = []
#for x in string.ascii_letters:
#    myList.append(ord(x))
#'''

#print(timeit.timeit(stmt=myStatement, setup=setup, number=10000))

#######################################################################################################################
# Exercise 3: Run these timeit examples and play with timings.  
# Try increasing the number that is inside the range() function for each
# copy of myList, and see how that effects the times from timeit.

#import timeit

#setup = '''import string, random
#base = string.ascii_letters + string.digits
#myList = [random.choice(base) for x in range(100)]
#'''

#statement_A = '''
#newList = []
#for i in myList:
#    if i not in newList:
#        newList.append(i)
#'''

#print(timeit.timeit(stmt=statement_A, setup=setup, number=10000))

#setup = '''import string, random
#base = string.ascii_letters + string.digits
#myList = [random.choice((random.choice(base), random.randint(0,25))) for x in range(100)]
#'''

#Statement_B = '''
#numbersOnly = []
#for item in myList:
#    if isinstance(item, int):
#        numbersOnly.append(item)
#'''

#print(timeit.timeit(stmt=statement_B, setup=setup, number=10000))


#if you'd like to mess with the command line app, type the following into your terminal:
#python3 -m timeit --help

#then try:
#python -m timeit -s "myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']" 'newList = []' 'for i in myList:' '    if i not in newList:' '        newList.append(i)'


#RESOURCES
#Timeit Docs:              https://docs.python.org/3.5/library/timeit.html
#PMotW takes on timeit:    https://pymotw.com/2/timeit/
#Python Profilers:         https://docs.python.org/3/library/profile.html

########################################################################################################################

# Exercise 4: Use the skills you just learned. Create a list with a mix of upper case and lower case letters
# And then use timeit to time your algorithm for filtering out the upper case letters.


########################################################################################################################
#PAUSE HERE FOR A WORD ABOUT WHAT IS PYTHONIC

#"Programs must be written for people to read,
#and only incidentally for machines to execute." -- Harold Abelson (Structure and Interpretation of Computer Programs)

#"Code is read much more often than it is written" -- Guido VanRossum
########################################################################################################################
#EXERCISE 5 - to get the zen of python
#UNCOMMENT THIS LINE!
#import this


#RESOURCES
#PEP8 (Code Formatting)            https://www.python.org/dev/peps/pep-0008/
#An alternate view on spaces       http://lea.verou.me/2012/01/why-tabs-are-clearly-superior/

#PEP202 (list comprehensions)      https://www.python.org/dev/peps/pep-0202/
#PEP274(dictionary comprehensions) https://www.python.org/dev/peps/pep-0274/
#PEP20 (The Zen of Python)         'import this' in the Python shell

########################################################################################################################
#PAUSE HERE FOR A WORD ABOUT LIST COMPHREHENSIONS

#Quick Examples of List Comprehensions

#this                                                                becomes

#symbols = '$¢£¥€¤'                                                  symbols = '$¢£¥€¤'
#codes = []                                                          codes = [ord(caracter) for character in symbols]
#for symbol in symbos:
#    codes.append(ord(symbol))


#this                                                                becomes

#results = []                                                        results = [num ** 2 if num % 2 == 0 else num ** 3 for num in range(1, 21)]
#for num in range(1, 21):
#    if num % 2 == 0:
#        results.append(num ** 2)
#    else:
#        results.append(num ** 3)


#Comprehensions in Python are syntactic constructs that allow sequences
#to be built from other sequences. Python3 (and Python 2.7.0++) come
#with different comprehension flavors:  List, Dictionary, and Sets.

#They're in the form of:

#[Output Expression  Input Sequence  Optional Predicate]

#Example:
#input_list = [1,2,3,4,5,6,7,8,9]
#output_list = []

#for item in input_list:              -->  this is the Input Expression        
	#if item%2 == 0:                  -->  this is the Predicate, or *Filter*  ----->  [item**2 for item in input_list if item%2==0]
	#	output_list.append(item**2)   -->  this is the Output Expression


#Of course, not everything can be (or should be!) compressed in this way.


#RESOURCES
#Thank you
#Bruce Eckel  -- Python3 Patterns & Idioms   http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
#Mark Pilgrim -- Dive into Python3           www.diveintopython3.net
#Obi Ike-Nwosu                               http://intermediatepythonista.com/python-comprehensions
#Python Foundation                           https://docs.python.org/3/howto/functional.html
#What's iterable?                            https://docs.python.org/3.5/glossary.html#iterable

#With exercises help from
#Trey Hunner                                 http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
#Boston Python                               http://puzzles.bostonpython.com/
#                                            github/zhiwehu/Python-programming-exercises

########################################################################################################################
#EXERCISE 6 - Rewrite this loop into a list comprehension (Bethany)
#Convert the first exercise into a comprehension

#my_list = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
#new_list = []

#for i in my_list:
#    if i not in new_list:
#        new_list.append(i)

#print(new_list)


#Solution:
#new_list = [x for x in my_list if my_list.count(x) < 2]
#print(new_list)
########################################################################################################################
#EXERCISE 7
# Convert this list and loop into a list comprehension


#input_list = [25, 8, 'C', 'l', 'Z', '7', 'l', 'g', 'u', 19, 14, 7, '7', 'o', 3, 17, 6, 21, 'q', 21, 'T', 6, 23, 'M', 'B', 9, 4, 22, 'w', 20, 'D', 'w', 'D', 7, '0', '7', 8, 'Z', 1, 18, 4, 'Q', 'W', 15, 'K', 13, 8, 'k', 0, 11]
#squared_numbers = []

#for item in input_list:
#	if isinstance(item, int):
#		squared_numbers.append(item**2)
#print(squared_numbers)

#Solution:

#squared_numbers = [number**2 for number in input_list if isinstance(number, int)]
#print(squared_numbers)


########################################################################################################################
#Exercise 8
# Convert this list/list comprehension into a list/loop:
#input_list = ['s', 'dd', 'v', 'TT', 'l', 'r', 'II', 'u', 'H', 'E', 'mm', 'qq', 'o', 'UU', 'nn', 'RR', 'YY', 'c', 'BB', 'P', 'ff', 'f', 'nn', 'bb', 'D', 'JJ', 'hh', 'k', 'y', 'F', 'J', 'dd', 'kk', 'JJ', 'L', 'jj', 'cc', 'f', 'P', 'KK', 'L', 'vv', 'CC', 'D', 'z', 'SS', 'L', 'E', 'r', 'b']
#doublecaps = [item for item in input_list if item.isupper() and len(item)>1]


#Solution:

#doublecaps = []
#for item in input_list:
#	if item.isupper() and len(item)> 1:
#		doublecaps.append(item)

########################################################################################################################
# Exercise  9
# Convert This list and loop into a list comprehension

#import string

#input_list = ['w', 8, 12, 4, 13, 'O', '7', 20, 'q', '3', 'v', 'E', '4', 1, 18, 1, 'e', 'I', 23, 'n', 12, 8, 3, 5, 5, 3, 21, 'H', 19, 14, 5, 'a', 'Z', 'Y', 23, 'g', 'p', 'Y', 'r', 'j', 'y', 'x', 0, '0', 16, 'U', 'S', 'k', 'D', 'D']
#numbers_and_letters = []

#for item in input_list:
#	if isinstance(item, int):
#		numbers_and_letters.append(item**2)
#	elif item.isalpha():
#		numbers_and_letters.append(item)


#Solution:
#import string
#numbers_and_letters = [item**2 if isinstance(item, int) else item if item.isalpha() else None for item in my_list]
########################################################################################################################
# Exercise 10
# Write a program which will find all numbers between 2000 and 3200 which are divisible by 7 but are not a multiple of 5.
# Output should be a list (try doing this with a comprehension)


#Solution:
#l=[]
#for i in range(2000, 3201):
#    if (i%7==0) and (i%5!=0):
#        l.append(i)

#OR

#l = [i for i in range(2000, 3201) if (i%7==0) and (i%5!=0)]

########################################################################################################################
# Exercise 11
# Write a function/comprehension which can compute the factorials of a list of numbers.
# The results should be returned in a list.

# Suppose the following input is supplied to the program:
# [7, 8, 9]

# Then, the output should be:
# [5040, 40320, 362880]

# Hint:  You can use the math module (math.factorial()) or write your own helper function
# Extras: Do it without calling the math module (Hint: try using reduce()), try using reduce() and operator.mul, try using only nested lists inside the comprehension.


#input_list = [6, 12, 5, 13]


#Solution #1 using the math module:

#from math import factorial
#solution = [factorial(x) for x in input_list]


#Solution #2 using helper functions:

#def fact(x): #recursive helper method
#    if x == 0:
#        return 1
#    return x * fact(x - 1)


#def fact(x):  #iterative helper method
#	factorial = 1

#	for number in range(1, x+1):
#		factorial = factorial*number
#	return factorial


#solution = [fact(x) for x in input]



#Extra Method #1 using a lambda:

#from functools import reduce
#solution = [reduce(lambda a, b: a*b, range(1, number+1)) for number in my_list]

#Extra Methond #2 using reduce() and operator.mul

#from functools import reduce
#from operator import mul
#solution = [reduce(mul, range(1, number+1)) for number in my_list]


#Extra Method #3 using list slices #do NOT do this at home!!:

#solution = [j for j in [1] for i in range(2, fac+1)for j in [j*i]][-1] for number in my_list]

######################################################################################################################

#EXERCISE A
# Jouella - PYTHON 3 FUNCTION CALLS ON STACK MEMORY  WRITING EFFECITENT LIST COMPREHENSIONS
# def add_two(n):
#   return n + 2
# x = [add_two(i) for i in range(10)]
# vs.
# y = [i + 2 for i in range(10)]

#EXERCISES - here
# tup1 = ('PyLadies', 'Oakland', 1, 2)
# tup2 = tup1

# tup1 is tup2 # True, look at id(tup1) & id(tup2)
# tup1 == tup2 # True

# tup1 = ('PyLadies', 'Oakland', 1, 3)
# id(tup1) # different
# tup1[0] = 'Hello' # will have a type error saying that it won't support item assignment



# ####################################################################################################################

# Exercise 13 (Alex) -
# Create a list of the months of a year 'jan', 'feb', .... ' dec'
# and use the tuple(myList) function to create a tuple of the list
# Mess around with the list methods, count, index, insert, pop, remove, reverse, append and sort
# Notice any differences between tuples and lists

# Background: You can change a list. You cannot change a tuple.
# Another way to say that is lists are mutable and tuples are immutable.
#
# Create a list and create a tuple both that represent the months of a year

# Answer 3
# myListMonths = ['January', 'Feb', 'march', 'april', 'may', 'june', 'july', 'august', 'sept', 'oct', 'nov', 'dec', 'Ja
# myTupleMonths = tuple(myListMonths)

# count
# lists
# count = myListMonths.count('January')
# print(count)
# Tuples
# count = myTupleMonths.count('January')
# print(count)

# index

######################################################################################################################
# Exercise 14 (alex)
# Exercise 3: Build a phone book only using lists (for this example the lists can be lists of tuples)
# Example: ("FirstName LastName", "312-999-9090") is an item in this list.

# Answer
# Lists of tuples
# phonebook = [
#    ("John Doe", "555-555-5555"),
#    ("Albert Einstein", "212-555-5555"),
# ]
# print(phonebook)

# phonebookNames = ['John Doe', 'Albert Einstein']
# phonebookNumbers = ['555-555-5555', '212-555-5555']
# print(phonebookNames[0])
# print(phonebookNumbers[0])
######################################################################################################################
# Exercise 15 (Alex) : Build a look up function for your address book
# Input is (phonebook - a list , name)
# Output is something like this "John Doe's phone number is 555-555-5555"

# Answer:
# phonebook = [
#    ("John Doe", "555-555-5555"),
#    ("Albert Einstein", "212-555-5555"),
# ]
# print(phonebook)

# def find_phonenumber(phonebook, name):
#    for n, p in phonebook:
#        if n == name:
#            return p
#        return None

# print("John Doe's phone number is", find_phonenumber(phonebook, "John Doe") )
######################################################################################################################
# (alex)
# Exercise 16 : Build a phone book using dictionary
# Example of a dictionary - but change this to a phonebook with names: Jane Doe and phone numbers 555-555-5555
# a = { 'x':1, 'y':2, 'z':3 }
# b = { 'w': 10, 'x': 11, 'y': 12 }
# Also, make a call to print out one example of name and phone number like
# Show that you can output something like this "John Doe's phone number is 555-555-5555" using your dictionary


# answer
# phonebook = {
#    "John Doe": "555-555-5555",
#    "Albert Einstein" : "212-555-5555",
# }
# print "John Doe's phone number is", phonebook["John Doe"]

######################################################################################################################
# DISCUSSION OF TWO OTHER EXAMPLES
# Vitamins and minerals that go with vegtables
# Shoes and sizes of shoes but you want to track the type of shoe
# Discussion of when to use a list and when to use a dictionary
# DISCUSSION OF USES of dictionaries

######################################################################################################################
# Exercise 17: Play with dictionaries - just use some of the basic functions
# Section on initialization - take from O'Reilly Python Pocket Reference by Mark Lutz
# Uncomment and play with this section so that you learn how to manipulate dictionaries

# Any immutable object can be a dictionary key (string, number, tuple)
# Class instances can be keys if they inherit hashing methods

# A two item dictionary: keys 'spam' and 'eggs'
# A = {'spam': 2, 'eggs':3}

# Nested dictionaries
# B = { 'info': {42: 1, type(''):2, 'spam':[]}}

# Creates a dictionary by passing keyword arguments to the type constructor
# C = dict(name='Bob', age=45, job=('mgr', 'dev'))

# Dictionary comprehension expression
# D = {c.upper(): ord(c) for c in 'spam'}
# print(D)
# print(ord('s'))

# E = {} # an empty dictionary

# Exercises for this section
# STEP 1 - Print out all of the keys for dictionary A
# print(A.keys())

# STEP 2 - Print out all of the values for dictionary D
# print(D.values())

# STEP 3 - play with the C.items() function.
# print(C.items())

# Step 4 - How would you clear all of the items from dictionary A?
# A.clear()
# print(A)

# Step 5 - Put the values back in A and do a copy (shallow copy) then change a value and print out both
# F = A.copy()
# print(F)
# F['spam'] = 4
# print(A)
# print(F)

# Step 6 - iterate through the dictionary D
# http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python
# for key, value in D.items():
#    print key, 'corresponds to', D[key]



#######################################################################################################################
#DICTIONARY COMPREHENSIONS - Bethany

#Remeber list comprehensions?  These are exactly the same, but for Dictionaries.
#One gotcha:  there are TWO variables that have to be used.  One for the key, one for the value

#To review lists:  [Output Expression(s)  Input Sequence(s)  Optional Predicate]
#What it looks like for a Dictionary:

#{keyExp(key): valueExp(value)  for key,value in Input Sequence if Optional Predicate}

#An Example  a Dictionary of all the numbers less than 1000 and greater than 49 tagged 
#as odd or even:

#{x:('odd' if x%2 !=0 else 'even')for x in range(1000) if x > 49}


#######################################################################################################################
#Exercise 18
#Using a dictionary comprehension, build a dictionary from the list of tuples below


#inventoryList = [('Black Pump', ['7.5', '8', '9', '11'])
#                 ,('Silver Flats', ['3','6', '7', '8', '9'])
#                 ,('White Tennies', ['8','9','10','10.5'])
#                 ,('Brown Roman Sandals', ['8', '8W', '9', '9W', '10', '10W', '13'])
#                 ,('Green Leather Pump', ['3','6', '7','9', '9W','12'])
#                 ,('Orange Slippers, Felt',['3','5','6','7','8', '8W', '9', '10W', '12'])
#                 ,('Red Lace Up Boots', ['3','8','9W','12'])
#                 ,('Black Flats', ['8', '8W', '9', '9W', '10', '10W', '13'])]



#Solution:
#myInventory = {value[0] : value[1] for value in inventoryList}



#######################################################################################################################
#Exercise 19
#Using a comprehension, create a Dictionary of the lower and uppercase English letters with their 
#corresponding Unicode Codepoint as the value.


#Solution
#import string
#uniDict = {key: ord(key) for key in string.ascii_letters}

#Now modify your answer so that only the vowels are listed.

#Solution
#import string
#uniDictVowels = {key: ord(key) for key in string.ascii_letters if key in 'aeiouAEIOU'}


#######################################################################################################################
#Exercise 20
#Using a comprehension, create a dictionary that lists all numbers under 100 whose cubes are divisible by 4.

#Solution
#cubies = {x: x**3 for x in range(100) if x**3 % 4 == 0}
#######################################################################################################################
#A BREIF LOOK AT PERFORMANCE of List vs Dictionary 

'''

setup = '''import string
uniList = [('a', 97), ('b', 98), ('c', 99), ('d', 100), ('e', 101), ('f', 102), ('g', 103), ('h', 104), ('i', 105), 
           ('j', 106), ('k', 107), ('l', 108), ('m', 109), ('n', 110), ('o', 111), ('p', 112), ('q', 113), ('r', 114), 
           ('s', 115), ('t', 116), ('u', 117), ('v', 118), ('w', 119), ('x', 120), ('y', 121), ('z', 122), ('A', 65), 
           ('B', 66), ('C', 67), ('D', 68), ('E', 69), ('F', 70), ('G', 71), ('H', 72), ('I', 73), ('J', 74), ('K', 75), 
           ('L', 76), ('M', 77), ('N', 78), ('O', 79), ('P', 80), ('Q', 81), ('R', 82), ('S', 83), ('T', 84), ('U', 85), 
           ('V', 86), ('W', 87), ('X', 88), ('Y', 89), ('Z', 90)]


uniDict = {'c': 99, 'M': 77, 'r': 114, 'q': 113, 'b': 98, 'f': 102, 'F': 70, 'o': 111, 'Z': 90, 'x': 120, 'S': 83, 
           'H': 72, 'U': 85, 'G': 71, 'i': 105, 'X': 88, 'O': 79, 'K': 75, 'z': 122, 'R': 82, 'L': 76, 'p': 112, 'C': 67, 
           'g': 103, 'u': 117, 'j': 106, 'y': 121, 'd': 100, 'e': 101, 'B': 66, 'n': 110, 'h': 104, 'Y': 89, 'W': 87, 
           'a': 97, 'Q': 81, 'k': 107, 'v': 118, 'l': 108, 'm': 109, 'T': 84, 'J': 74, 'E': 69, 'V': 86, 'P': 80, 'w': 119, 
           'I': 73, 'A': 65, 'D': 68, 't': 116, 'N': 78, 's': 115}

lookup = ['A', 't', 'w', 'Y', 'x', 'R', 'v', 'b', 'T', 'a', 'B', 'A', 't', 'w', 'Y', 'x', 'R', 'v', 'b', 'T', 'a', 'B']           
'''

statement_G = '''
code = []
for letter in lookup:
    for item in uniList:
        if item[0] == letter:
            code.append(item[1])
'''

statement_H = '''
code = []

for letter in lookup:
    code.append(uniDict[letter])
'''

#print(timeit.timeit(stmt=statement_G, setup=setup, number=10000))
#print(timeit.timeit(stmt=statement_H, setup=setup, number=10000))


'''
#######################################################################################################################

#######################################################################################################################
# Discussion - (alex)
# Concept of a hash table
# Concept of open addressing (one object per bucket) and chaining (linked list in each bucket)
# Lookup for a dictionary is constant because O(n) lookup and O(1) for insertion

# A unique object that can
# https://wiki.python.org/moin/TimeComplexity
#######################################################################################################################

# Excercise 18 - very simple hash table for illustration and discussion (alex)
# STEP 1 - play with this and understand it
# STEP 2 - write something to handle collisions. So, you could put a list into the value and add to the list
# everytime there was a collision. That is chaining.
# So, lists can be the values, but lists of lists can't be the values. Values must be hashable.
# Example of something that is unhashable - another list. lists are mutable. if a datatype is mutable it is not hashable
# Because you can't reduce it to a unique value because it might change and the hash funciton would change.

'''
import re

class HashTable:
    myHashTable = []

    def __init__(self):
        self.myHashTable = [None] * 1000

    def addToHash(self, name):
        index = self.hashIt(name)
        self.myHashTable[index] = name


    def printHashTable(self):
        for i, val in enumerate(self.myHashTable):
            if val is not None:
                print(i, val)

    def hashIt(self, value):
        #Take the first three letters of the string
        #Get the ord('f') of each of these first three chars
        #Add these
        #return the hash for hashing
        regExString = r'^[A-Za-z]{3}$'
        m = re.match(regExString,value)
        if m is not None:
           a = ord(value[0])
           b = ord(value[1])
           c = ord(value[2])
           d = a + b + c
           print(str(a) + " " + str(b) + " " + str(c) + " " +  str(d))
        else:
            print(str + " Failed input - this function only takes 3 letters")

        return d


myHash = HashTable()
myHash.addToHash('foo')
myHash.addToHash('boo')
myHash.addToHash(('cry'))
myHash.addToHash('oof')
results = myHash.printHashTable()
print(results)

'''

#######################################################################################################################
# ALEX
# Exercise 19 - Illustrate the difference between a hash table and a set. (review dictionary )
# Sets are just hashtables without values or dictionaries without values. Lists are resizable arrays that track
# What can go in a list can be unhashable

# excecise X - Dedup the list from the beginning using a set

# myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
# mySet = set(myList) #Because it is using a hash funciton, this is O(n)
# print(mySet)


# Excercise X
# myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
# myOtherList = ['c', 'c', 'a', 'z', 'p', 'q', ]
# myListIsNowASet = set(myList)
# myOtherListIsNowASet = set(myOtherList)
# intersaction = myListIsNowASet&myOtherListIsNowASet
# print(intersaction)
# https://docs.python.org/2/library/stdtypes.html#set
#######################################################################################################################

#SET COMPHREHENSIONS - Bethany DISCUSSION

#Set comprehensions look like list comprehensions, but with {}:

#Example -- a set of the squares of numbers 1-10:
#nums = {n**2 for n in range(1, 11)}

#alternatively, you can call the set construtor:

#set(n**2 for n in range(1,11))

#######################################################################################################################

#BETHANY - SET COMPREHENSIONS
# Set Comprehensions - fluent programming book
# Comphrehension of a set
#some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#duplicates = set(x for x in some_list if some_list.count(x) > 1)
#print(duplicates)


#######################################################################################################################
#ALEX - DISCUSSION
# ABUSES Of Dictionaries

'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
deduped = []

for value in some_list:
    if value not in deduped:
        deduped.append(some_list.pop(some_list.index(value)))

print(deduped)
print(some_list)
'''

# Adding a new item to a dictionary can cause the hash table to change. During this process, the keys might
# change their order in the underlying datastructure. You can't reliably predict what or when this will happen.
# If you are iterating over the dictionary keys and changing them at the same time, your loop may
# not scan all of the items as expected.
# Best Practice - If you need to scan and update items to a dictionary, do it in steps
# 1. Read the dict from start to finish and collect the needed updates in a second dict
# 2. Update the first one with the second one in a separate move

######################################################################################################################
#EXERCISE 20 - Take this phonebook dictionary and write a function that find duplicate phone numbers (they must be
# roommates in those cases) and then update the keys to read LastName1 - LastName2 Household
phonebook = {
    "Marie Curie": "555-555-5555",
    "Rosalind Franklin" : "212-555-5555",
    "Lise Meitner" : "212-555-5555",
    "Chien-Shiung Wu" : "555-555-5555",
    "Rita Levi-Montalcini" : "510-908-1234",
    "Barbara McClintock" : "415-987-4313",
    "Gertrude B. Elion" : "757-698-1234",
    "Ada Lovelace" : "614-987-1456"
}
#print("Ada's phone number is", phonebook["Marie Curie"])

# So, the result for Marie Curie and Chien-Shiung Wu would be "Curie-Wu Household" : "555-555-5555
# This way we would only have one entry per household. (They share a phone)
#However, make this change following the best practice above and avoiding an abuse of dictionaries, which is changing
#dictionary keys (changing the hashtable) at the same time that you are iterating through it


########################################################################################################################

#DISCUSSION - 2nd ABUSE OF DICTIONARIES
# - DICS ARE NOT SPACE EFFECIENT - A dictionary is in memory
# For example, if you are handling a large quantity of records,
# it makes sense to store them in a list of tuples or named tuples instead of using a list of dictionaries in
# JSON style, with one dict per record. Replacing dicts with tuples reduces the memory usage in two ways:
# by removing the overhead of one hash table per record and by not storing the field names again with each record.

#######################################################################################################################

#EXERCISE B
#JOUELLA

# from http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#list-comprehensions
# exercise: try to convert this
# new_list = []
# for item in a_list:
#    if condition(item):
#       new_list.append(fn(item))
# to pythonic


#######################################################################################################################

#A WORD ON THE COLLECTIONS MODULE - BETHANY

#######################################################################################################################
#COUNTER - DISCUSSION

#A Counter is a dict subclass for counting hashable objects.  Its a dictionary
#where the elements are stored as keys, and their counts are stored as the
#dictionary values.  Counts are allowed to be any integer value **including**
#zero or negative numbers.  Counters are similar to the bags or multisets of 
#other programming languages.

#Counters have two special methods beyond the standard dictionary methods:

#elements() -- returns an iterator over all elements, repeating each as many times as Its
              #count value.

#most_common() -- returns a list of the n most common elements and their counts, sorted
               #  from most common to least.  If n is not specified, *all* elements from the
               #  Counter are returned.

#######################################################################################################################
#COUNTER EXERCISES
#EXERCISE 21 - Bethany
#write a short function to find out if each phrase pair are anagrams of one another:
#Hint:  This can be done in two lines of code, but watch out for readablity.

#words_list = [('parliament', 'partial men'),  
		   ('listen', 'silent'), 
		   ('Clint Eastwood', 'Old West Action'), 
		   ('Berkeley', 'Rebel Keys'), 
		   ('Dormitory', 'Dirty Room'),
		   ('Desperation', 'rope ends it'),
		   ('Tom Cruise', 'So Im cute'),
              ('Conversation', 'Voices rant on')]


#Solution
#from collections import Counter

#makes a new list of tuples with spaces between words eleminated
#clean_list = [(item[0].replace(' ', ''), item[1].replace(' ', '')) for item in words_list]

#creates a list that compairs the Counter of one  phrase to a Counter of another
#result=[Counter(item[0].lower()) == Counter(item[1].lower()) for item in clean_list]

#print(result)

#######################################################################################################################
#EXERCISE 22 (bethany)
#Count all the words in the paragraph below, and then print
#them out in a list sorted from most frequent appearance to 
#least frequent appearance.

#Hint:  The output can be a list of Tuples here -- OR just the words in frequency order
#Warning: Remember that some words are capitalized, yet the same as other words
#         Keep in mind that not all whitespace is created equal, and '--' is not a word

#paragraph = """
#Four score and seven years ago our fathers brought forth on this continent, a new nation, 
#conceived in Liberty, and dedicated to the proposition that all men are created equal.
#
#Now we are engaged in a great civil war, testing whether that nation, or any nation so 
#conceived and so dedicated, can long endure. We are met on a great battlefield of that 
#war. We have come to dedicate a portion of that field, as a final resting place for 
#those who here gave their lives that that nation might live. It is altogether fitting 
#and proper that we should do this.
#
#But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow 
#-- this ground. The brave men, living and dead, who struggled here, have consecrated it, 
#far above our poor power to add or detract. The world will little note, nor long remember 
#what we say here, but it can never forget what they did here. It is for us the living, rather, 
#to be dedicated here to the unfinished work which they who fought here have thus far so nobly 
#advanced. It is rather for us to be here dedicated to the great task remaining before us -- that
#from these honored dead we take increased devotion to that cause for which they gave the last 
#full measure of devotion -- that we here highly resolve that these dead shall not have died in 
#vain -- that this nation, under God, shall have a new birth of freedom -- and that government of 
# the people, by the people, for the people, shall not perish from the earth.
#"""

#Solution

#import string
#import re
#from collections import Counter

#note the generator form here -- I don't need an itermediate list, so I don't have Python make one
#def word_count(paragraph):
#        counts = Counter((re.sub('\W+','', item).lower() for item in paragraph.split()))
#        return counts.most_common()

#print (word_count(paragraph))

#######################################################################################################################
#EXERCISE 23
#Take the same exercise from above, but instead of printing the words in frequency
#order, print a list of the words grouped together (sorted or not). So all the 
#'a' strings, follwed by all the 'above' strings, etc.  

#Hint:  you can call sorted() on any iterable.

#Solution:
#import string
#import re
#from collections import Counter

#note the generator form here -- I don't need an itermediate list, so I don't have Python make one
#def word_count_repeat(paragraph):
#        counts = Counter((re.sub('\W+','', item).lower() for item in paragraph.split()))
#        
#        return sorted(counts.elements())

#print (word_count_repeat(paragraph))

#######################################################################################################################
#Exercise C:
# JOUELLA - NAMED TUPLES
# from collections import namedtuple
# Person = namedtuple('Person', 'name age height')
# Person = namedtuple('Person', 'name age height', verbose=True), will print out the class definition
# mara = Person(name='Rooney Mara', 'age=26, height=5.2)

#######################################################################################################################


#EXTRA CREDIT THINGS TO THINK ABOUT - THE END OF THE TUTORIAL
#FIND THE MOST Efficient solution for deduping a large list. I want a list of the duplicates and a debbed list and i don't
#want duplicates in the dubbed list

#MARKOV CHAINS and dictionaries
#http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
