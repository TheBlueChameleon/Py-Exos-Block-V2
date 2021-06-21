# ============================================================================ #
# problem 1

import random

print("### Selection Sort")

def selectionSort(data) :
  for k in range(len(data)) :
    x, i = min([(x, i) for (i, x) in enumerate(data[k:])])         # get the smallest element and its index with this line. See below for some more comments
    data[k], data[k + i] = data[k + i], data[k]
  

data = random.sample(range(100), 5)

print("unsorted data")
print(data)

selectionSort(data)

print("for comparison: data sorted by python")
print(sorted(data))

print("sorted data")
print(data)

# on line 10:
# deconstruct this line: 
# data[k:] gives the sub-list of data, starting at the k-th element, and up to 
#   the last one.
# enumerate(<some list>) gives (something like) a list, comprising of tuples.
#   These tuples are of the form (i, x), where i is the index of x in the 
#   container <some list>.
# [f(x) for x in <some list>] is list comprehension.
#   we create a new list where each item in the new list is computed from the 
#   elements in the old list.
#   f(x) tells what to compute exactly.
# x, y = <tuple> is the syntax for tuple unpacking. If <tuple> comprises two
#   values, then x will be a copy of the first value and y a copy of the
#   second one.
# So, the list comprehension part makes a list of tuples. The first element of
#   each tuple is the element in the original list data[k:], and the second one
#   is the associated index in data[k:].
#   Note how the order is flipped in the list comprehension:
#   (x, i) for (i, x) in ...
#   enumerate generates tuples where the index is first; the list comprehension
#   generates tuples where the value is first!
# min(<some list>) finds the smallest object in <some list>. What is considered
#   the smallest element depends on the type of objects in <some list>.
#   Here, we have tuples (x, i) in the list data[k:].
#   When comparing two tuples, Python goes by lexicographic sorting: it first
#   compares the two first elements of two tuples, then their second elements,
#   and so on.
#   For example, if you have
#     (x, y) < (a, b)
#   then Python will first compare x with a. If x < a, then this returns True.
#   if x > a, this returns False.
#   if x == a, then Python goes on to compare y and b.
#   Hence, min finds the tuple with the smallest x, i.e. the samllest value of
#   data[k:], along with its associated index i.
# x, i = <tuple> again is tuple unpacking: we get the smallest value x of 
# data[k:] and its index i.


# another way to solve this is the method index in the class list:
# index returns the index of a given value (provided the value is in the list)
# we can use min to get the smallest value and then index to find its location.
# Note that this solution has bad runtime behaviour: We go through the entire 
# list a first time to find the smallest value, and then a second time again to
# find its index.

minIdx = data.index(min(data))


# if you find this too complicated, you might want to use a function that finds
# the index of the smallest element of a function, like the one below:

def minIndex(data) :
  minCandidate = data[0]
  minIndex     = 0
  for i in range(1, len(data)) :
    if data[i] < minCandidate :
      minCandidate = data[i]
      minIndex     =      i
  
  return minIndex

# this is also the fastest method in terms of runtime as it requires only one
# go through the list to achieve its goal.

print(minIdx, minIndex(data))   # regardless of the method applied, this will
                                # always output 0 0 after sorting.

# ============================================================================ #
# problem 2

print("### antiderivative")

import math

def antiderivative(func, N = 1000) :
  def integrate(stop) :
    result = 0
    width  = stop / N
    
    for i in range(N) :
      x = i * width
      result += func(x) * width
    
    return result
  return integrate

theCos = antiderivative(math.sin)

# pseudo-graphical representation:

for x in range(20) :
  print( int(theCos(x / 3) * 10 + 20) * " ", "*")
print()

# This solution is horrible when it comes to efficiency, but the aim of this
# is going through ideas of scope/visibility/data flux.
# Consider taking the lectures Numerial Recipies (Solbrig, Winter Terms, focus 
# on coding aspects) or Numerics (various lecturers, Winter Terms, focus on
# maths) if you're more interested
