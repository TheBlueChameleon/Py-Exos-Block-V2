# ============================================================================ #
# problem 1

def crossSum(x) :
  if type(x) != int :
    print("Only defined for integers")
    return
  
  result = 0
  if (x < 0) :
    print("Only defined for positive integers")
    return
  
  while x :
    result  += x % 10
    x      //=     10
    
  return result

print( crossSum(543) )
print( crossSum("five hundred") )
print( crossSum(-543) )

# take a look at line 5:
# we may pass *any* object as argument x. However, in the function we assume 
# that x is an integer, i.e. that we can divide it by 10 and that, after a 
# number of repetitions, this will give 0.
# That means we manually test whether x is really an integer and deny service
# if not.

# ============================================================================ #
# problem 2

# Locally, i.e. within the scope of swap, this actually does perform a triangle
# exchange. That means, the local variables x_swap and y_swap now reference 
# memory cells such that they have the other variables initial value.
# However, this is disconnected from the state of the module level: neither 
# x_main nor y_main "see" any of the effects done to x_swap and y_swap.
# 
# memory model:
#
# --------+--------+--------+--------+--------+--------+--------+--------+------
#    100  |   101  |   103  |   104  |   105  |   106  |   107  |   108  |  ...
#  x_main | y_main | x_swap | y_swap |        |        |        |        |
#  -> 105 | -> 106 | -> 107 | -> 108 |    2   |    3   |    3   |    2   |
#
# (rows in this picture signify: memory address, variable name, content of the
# memory cell)

# ============================================================================ #
# problem 3

print("FIZZBUZZ")

substitutions = {
  3 : "Fizz",
  5 : "Buzz",
  7 : "Tess"
}

# ............................................................................ #
# solution as a function, returning a list

def makeFizzBuzzList(N, substitutions) :
  reVal = []
  for i in range(1, N+1) :
    special = ""
    for divisor, substitute in substitutions.items() :
      if i % divisor == 0 :
        special += substitute
        
    if special : 
      reVal.append(special)
    else :
      reVal.append(str(i))
  
  return reVal
# ............................................................................ #
# simple on-screen solution

N = 35

for i in range(1, N+1) :
  special = False
  for divisor, substitute in substitutions.items() :
    if i % divisor == 0 :
      print(substitute, end="")
      special = True
      
  if not special : 
    print(i, end="")
    
  print(", ", end="")
  
print("...")

print(makeFizzBuzzList(N, substitutions))
print()

# ============================================================================ #
# problem 4

print("RANDOM WALK")

import random

runs   = 500            # how often to send the drunkard down the road
N      = 20             # how many steps to take
B      = 10             # width of the road
pLeft  = 0.5            # bias to the left (go left 100% of the time --> 1)
drifts = [0] * runs     # result of all runs: in the i-th run, the drunkard has gone drifts[i] steps to the left. Negative values indicate steps to the right.

# |-------------------------|
# 0                 x       1

for run in range(runs) :
  drift  = 0
  for step in range(N) :
    r = random.uniform(0, 1)
    
    if r < pLeft :                      # take a step to the left
      if drift != -B : drift -= 1
    else :                              # take a step to the right
      if drift != +B : drift += 1
  
  drifts[run] = drift

histogram = {d : drifts.count(d) for d in range(-B, B+1)}

for d, v in histogram.items() :
  print(f"{d:+3}", "#" * v)
print()

# ============================================================================ #
# problem 5

print("PI MONTE CARLO APPROXIMATION")

import random         # already imported from task 2, but importing it a second time does precisely nothing

def getPi(accuracy) :
  N = 0
  
  for run in range(accuracy) :
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    
    if x*x + y*y < 1 : N += 1
  
  return 4 * N/accuracy

for p in range(10, 15) :
  accuracy = 2**p
  print(f"accuracy: {accuracy:7}, pi ~ {getPi(accuracy)}")

print()

# ============================================================================ #
# problem 6

print("ERATOSTHENES PRIME SIEVE")

N = 10000

data = [i for i in range(2, N+1)]

for i in data :
  if i == 0 : continue
  
  for j in range(i+i, N+1, i) :
    data[j-2] = 0

for i in data :
  if i : print(i, end=", ")
print("...")

print()

# ============================================================================ #
# problem 7

print("TEXT TO LIST")

dataStr = "1,2, 3,     4.5   , 7777" # input("Bitte eine Komma-getrennte Liste eingeben: ")
dataNum = [float(datapoint.strip()) for datapoint in dataStr.split(",")]

print(dataNum)
