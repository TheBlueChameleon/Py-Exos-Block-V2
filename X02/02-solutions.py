# ============================================================================ #
# Problem 1

import math
import cmath

aStr = input("Please provide a number a:")
bStr = input("Please provide a number b:")
cStr = input("Please provide a number c:")

print("REAL VALUED TREATMENT:")
a = float(aStr)
b = float(bStr)
c = float(cStr)

discr = b**2 - 4 * a * c

if discr == 0 :
    x = -b / (2*a)
    print("There's one solution: x =", x)
    
elif discr > 0 :
    x_1 = (-b + math.sqrt(discr)) / (2*a)
    x_2 = (-b - math.sqrt(discr)) / (2*a)
    
    print("There are two solutions:")
    print("  x_1 =", x_1)
    print("  x_2 =", x_2)
else :
    print("There's no solution!")


print("COMPLEX VALUED TREATMENT:")
a = complex(aStr)
b = complex(bStr)
c = complex(cStr)

discr = b**2 - 4 * a * c

if discr == 0 :
    x = -b / (2*a)
    print("There's one solution: x =", x)
else :
    x_1 = (-b + cmath.sqrt(discr)) / (2*a)
    x_2 = (-b - cmath.sqrt(discr)) / (2*a)
    
    print("There are two solutions:")
    print("  x_1 =", x_1)
    print("  x_2 =", x_2)


# ============================================================================ #
# Problem 2

# factorial returns n! = n * (n-1) * (n-2) * ... where n is an integer
# radians converts degrees (0..360°) to radians (0..2pi)
# index searches an element in a list and returns the index of the element IF it
#   can be found. Otherwise, a ValueError is triggered (this will be covered 
#   later in detail. In brief: program execution is aborted with an error 
#   message)
# clear deletes all objects in a list

# This can be illustrated as follows

import math

myList = ["Dusky", "Joe", "Hartington"]

print("### ELEMENTS IN MODULE MATH:")
print(dir(math))
print()

print("### ELEMENTS IN CLASS LIST:")
print(dir(myList))

print( math.factorial(4) )       # Output 24 = 4 * 3 * 2 * 1
print( math.radians(180) )       # Output 3.141592653589793 (also pi)
print( myList.index("Joe") )     # Output 1 (Index of 'Joe')
#print(myList.index("nobody"))   # triggers an error message
myList.clear()
print(myList)                    # Output [] -- myList is still a list!


# ============================================================================ #
# Problem 3

stringVar = "My Hovercraft is full of eels"
everySecond = stringVar[1::2]
wordsInList = stringVar.split()

print(everySecond)
print(wordsInList)

# ============================================================================ #
# Problem 4

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matrix[0])
print(matrix[1])
print(matrix[2])

matrix[2][0] = -7               # Change row 3, column 1

# ============================================================================ #
# Problem 5

book = [["Peter", 19, 1.80], ["Jasmin", 20, 1.63], ["Alex", 22, 1.93]]
book.sort()

print(book)

# Currently, to change the sorting criterion you can only do this by changing 
# the order in which the list elements are arranged. I.e. put the age before the
# names:
# book = [[19, "Peter", 1.80], [20, "Jasmin", 1.63], [22, "Alex", 1.93]]

# ============================================================================ #
# Problem 6

vector_a = [ 3, 2, 1, 5, 7, 2, -1]
vector_b = [-7, 3, 7, 5, 6, 8,  1]

result = 0
for i in range(len(vector_a)) :
  result += vector_a[i] * vector_b[i]

print(result)

# ============================================================================ #
# Problem 7

text = "the quick brown fox jumps over the lazy dog"
uniqueChars = set(text)
sortedChars = sorted(uniqueChars)

# automatic version
autoCounts = {char : text.count(char) for char in uniqueChars}

# manual version
counts = {char : 0 for char in uniqueChars}       # initialize dict with start values 0

# alternatively:
#counts = dict()
#for char in uniqueChars :
#  counts[char] = 0

for char in text :                                # count manually
  counts[char] += 1

print("Analysis of '" + text + "':")
for char in sortedChars :
  print(char, "appears", counts[char], "times; automatic count yields:", autoCounts[char])

# ============================================================================ #
# Problem 8

# ---------------------------------------------------------------------------- #
# Approach 1

height = 7

for row in range(height) :
  print(" " * (height - row - 1), "*" * (2 * row + 1))
print()

# ---------------------------------------------------------------------------- #
# Approach 2


for row in range(height) :
  for column in range(height - row) : print(" ", end="")
  for column in range(2 * row + 1)  : print("*", end="")
  
  print("")

# ---------------------------------------------------------------------------- #
# Approach 3

for   row    in range(    height    ) :
  for column in range(2 * height + 1) :
    starFlag = abs(column - height) < (row + 1)
    
    print("*" if starFlag else " ", end="")
  print("")

# ---------------------------------------------------------------------------- #
# Approach 4

width = 2 * height + 1
for i in range(height * width) :
    row = i / width
    col = i % width
    
    if ((col <= height - row) or (col >= height + row)) : print(" ", end="")
    else                                                : print("*", end="")
    
    if (col == width - 1) : print("")

# ============================================================================ #
# Problem 9

# Depending on the chosen approach you'll find two (possibly even more...)
# different yet *correct* results. There are multiple ways to break a rod that
# influence the resulting probability.
# Here, we don't want to go too deep into the subtleties of stochastics but 
# focus on the coding techniques.

# Basic idea:
# To form a triangle, the condition has to be satisfied: The longest piece
# has to be shorter than the other two combined.
# This is equivalent to:
# The longest piece must be shorter than half the entire rod

# ---------------------------------------------------------------------------- #
# Approach 1
# Pick three lengths a, b, c, as recommended on the problem paper.
# I.e. we first break a piece a of random length off the whole rod (length 1).
# After that, we break off a piece b of random length of the remainder of the
# rod (length 1-a).
# What is left then gives piece c = 1 - (a+b)
# Result: ca 0.193

import random

hits =    0
N    = 5000

for n in range(N) :
  a = random.uniform(0, 1)
  b = random.uniform(0, 1 - a)
  c = 1 - (a+b)

  lengths = sorted([a, b, c])
  
  if lengths[0] + lengths[1] > lengths[2] :
    hits += 1
  
print(hits / N)

# ---------------------------------------------------------------------------- #
# Approach 2
# Pick two *points* x, y at which the rod is broken. From this, compute the 
# lengths.
# Since point y may be located before x, we get a hidden additional choice after
# breaking the off the first piece: either we break piece b off the remainder
# (lenght 1-a, as before), or we break b off of a. This is why there are two
# different yet corret results.
# Result: ca. 0.25

hits = 0
for n in range(N) :
  x = random.uniform(0, 1)
  y = random.uniform(0, 1)

  x, y = sorted([x, y])

  a = x
  b = y - x
  c = 1 - y

  lengths = sorted([a, b, c])

  if lengths[0] + lengths[1] > lengths[2] :
    hits += 1

print(hits / N)


# ============================================================================ #
# Bonus Problem

# Internally, everything is references! In line 1 we create an empty list. In
# this, we add the list A itself *as a reference*, i.e. A contains itself, but
# not as a copy. Think of a piece of paper on which it is written how to find
# the piece of paper.
# 
# Memory model:
# -+-----------------------------+---------------------
#  | Element 0 of A:             |
#  | reference to memory cell X  |
# -+-----------------------------+---------------------
#   \                           /
#    \      memory cell X      /
# 
# Accordingly, reading A[0] yields A itself: the piece of paper is read, and you
# find some information; only that the found information is the same information
# you had before: A itself is a refrence to a memory cell as well.
# You can go to arbitrary depths: A == A[0] == A[0][0][0]...[0].
# 
# When overwriting (A[0][0] = 1) the list element with index 0 is changed, i.e.
# a new reference is put there:
# 
# -+-----------------------------+------+--------------
#  | Element 0 of A:             |   1  |
#  | reference to memory cell Y  |      |
# -+-----------------------------+------+--------------
#   \                           / \    /
#    \      memory cell X      /     Y
# 
# The original structure of the list A in memory is kept as is.
