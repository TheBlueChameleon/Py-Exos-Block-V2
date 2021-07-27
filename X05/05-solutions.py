# ============================================================================ #
# problem 1

print("### Characters in a file")

with open("praktische_Physik.txt", "r") as handle :
    content = handle.read()

# manual approac:
total = len(content)
chars = 0
words = 1
lines = 1

for char in content :
    if char == " " :
        words += 1
    
    if char == "\n" :
        words += 1
        lines += 1
    else :
        chars += 1

print("COUNT MANUALLY:")
print("characters toal    :", total)
print("without line breaks:", chars)
print("words              :", words)
print("lines              :", lines)
print()


# let Python do the tedious work:
with open("praktische_Physik.txt", "r") as handle :
    content = handle.readlines()

lines = len(content)
total = sum(len(line)       for line in content)
chars = sum(len(line) - 1   for line in content) + 1          # - 1: line breaks are part of the variable line. + 1: there's no line break in the last line.
words = sum(line.count(" ") for line in content) + lines      # + lines: each line begins with a word in front of which there is no whitespace.

print("ZWEITE AUSZÄHLUNG:")
print("characters toal    :", total)
print("without line breaks:", chars)
print("words              :", words)
print("lines              :", lines)

print("=" * 80)

# ============================================================================ #
# problem 2

print("### File size with tell and seek")

with open("praktische_Physik.txt", "rb") as handle :
    handle.seek(0, 2)     # jump to end of file
    lof = handle.tell()

print("Length in bytes:", lof)

print("=" * 80)

# ============================================================================ #
# problem 3

print("### Total Score")

import csv

# purely with the means shown in the lecture:
with open("gameScores.txt") as handle :
    reader = csv.reader(handle)
    
    lines = []                        # read the file into a buffer
    for line in reader :
        lines.append(line)

scores = {}                           # create an empty dict
for i, name in enumerate(lines[0]) :  # first line holds 'headlines' which we use as keys for our dict
    scores[name] = sum( int(score[i]) for score in lines[1:] )

for name, score in scores.items() :
    print(f"{name:5}: {score} points")
print()

# another way:
with open("gameScores.txt") as handle :
    reader = csv.reader(handle)
    
    names = next(reader)
        # the fucntion next hasn't been covered yet.
        # next takes an iterable (i.e. an object that can be iterated over with
        # for), and returns the next element in the container.
        # Not every iterable can be accessed with indices, e.g.
        #   names = reader[0]
        # won't work. Hence, we need this workaround to fetch the headlines
        # outside of a loop.
        # 
        # The subsequent for loop catches up where next has left the iterable,
        # i.e. the head line has been skipped.
    
    scores = {name : 0 for name in names}
    
    for line in reader :
        for i, points in enumerate(line) :
            scores[names[i]] += int(points)

for name, score in scores.items() :
    print(f"{name:5}: {score} Punkte")

# ============================================================================ #
# problem 4

print("### Integral (I)")

import math

def integrate(func, start, stop, N) :
  result = 0
  width  = (stop - start) / N
  
  for i in range(N) :
    x = start + i * width
    result += func(x) * width
  
  return result

print( integrate(math.exp, 0, 1, 10000) )

# ============================================================================ #
# problem 5

print("###  N-Fold Concatenation")

def func(x) :
  return x + 1

def nFach(f, N, x) :
  arg = x
  for i in range(N) :
    arg = f(arg)
  return arg

print( nFach(func, 3, 0) )


# recursive version:

def nFold(f, N, x) :
  if N == 0 : return x
  else      : return f(nFold(f, N-1, x))
