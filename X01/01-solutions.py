# ============================================================================ #
# Problem 1

# free point for you. If you get your interpreter and some code editor to work
# you've made it ;)

# ============================================================================ #
# Problem 2

# i is int, 
# f is float,
# s is String.
# i + i is still int
# i + f is float (Python tries to preserve as much information as possible)
# i * s is string ("22" -- definition of multiplication of strings)
# f * s triggers an error message, since Python does not know what to do whith 
#   fractions of strings.

# ============================================================================ #
# Problem 3

complexNumber = 1j

# alternatively:
complexNumber = complex(0, 1)

print(complexNumber**2, complexNumber.real, complexNumber.imag)
# Output:
# (-1, 0) 0 -1

# the latter two extract -- surprise -- the real and imaginary part of the
# complex number, as a float

# ============================================================================ #
# Problem 4

text = '"That' + "'s a pity" + '", she said.'

# alternatively:
text = '"That\'s a pity", she said'

print(text)

# ============================================================================ #
# Problem 5

b = 3
h = 4
i = 5

z = (i // b) + 1
s = (i %  b) + 1

print("Row", z, ", Column", s)

# ============================================================================ #
# Problem 6

number = float(input("Bitte geben Sie eine Zahl ein: "))
print(2 * number)

# ============================================================================ #
# Problem 7

print(f"{22/7:5.3f}")

# Funny side note: The value 22/7 is sometimes cited as a "good approximation
# for pi"
# At least in engineering context, this is sometimes really used. Also, 22 July
# is sometimes celebrated as "alternative pi day" for that reason, (next to
# March 14, of course)

# ============================================================================ #
# Problem 8

x = float(input("Please provide a number: "))

if x**2 - 49 == 0 :
    print("Your input is a solution to x^2 - 49")
else:
    print("Your input is no solution to x^2 - 49")

# ============================================================================ #
# Problem 9

year = int(input("Please provide a year: "))

if         year %   4 == 0 :
    if     year % 100 == 0 :
        if year % 400 == 0 :
            print("leap year")
        else :
            print("no leap year")
    else :
        print("leap year")
else :
    print("no leap year")


# Alternativ auch:

if (year % 400 == 0 or (year % 4 == 0  and year % 100 != 0)) :
    print("ist leap year")
else :
    print("ist no leap year")

# oder

leapYear = False
if   year % 400 == 0 :
  leapYear = True
elif year % 100 == 0 :
  leapYear = False
elif year %   4 == 0 :
  leapYear = True
else :
  leapYear = False

print(f"The year {year} is", "a" if leapYear else "no", "leap year")
