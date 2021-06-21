import numpy as np
import matplotlib.pyplot as plt

# ============================================================================ #
# problem 1

X = np.linspace(-3, 3, 201)
Y = np.exp(-X**2) * np.sin(10 * X)

plt.plot(X, Y)
plt.show()

# ============================================================================ #
# problem 2

N = 18
diagonalTerms = 50 * np.arange(1, N+1)
couplingTerms = 10 * np.array([(i + 1) // 2 if (i + 1) % 2 == 0 else 0 for i in range(1, N)]) 

mat = np.diag(diagonalTerms) + np.diag(couplingTerms, 1) + np.diag(couplingTerms, -1)

print(mat)
print()

# ============================================================================ #
# problem 3

# the givens
money   = 10.0
names   =          ["dark chocolate", "milk chocolate", "caramel nuts bar", "coco cubes", "mint drops"] 
prices  = np.array([            1.0 ,             0.9 ,               2.3 ,         1.5 ,          0.3])
weights = np.array([              5 ,               4 ,                12 ,           8 ,            1])
N       = len(names)

# construction of the meshgrid
upperLimits = money // prices                               # upper limits: this many elements can be bought if we limit ourselves to a single sort of sweets
values = tuple([np.arange(u + 1) for u in upperLimits])     # tuple of lists: each lists goes from 0 to N_sweet ...
meshgrid = np.meshgrid(*values)                             # ... which can be used to build the mesgrid from this.

# rempark: 
#   *tuple
# automatically unpacks a tuple. Hence,
#   np.meshgrid(*values)
# is the same as
#   np.meshgrid(values[0], values[1], ...)

# Find the cost for each configuration ...
totalMoney = np.zeros(meshgrid[0].shape)
for i, price in enumerate(prices) :
    totalMoney += price * meshgrid[i]

# ... and the point score as well
totalScore = np.zeros(meshgrid[0].shape)
for i, score in enumerate(weights) :
    totalScore += score * meshgrid[i]

# which configurations can we actually afford?
mask = totalMoney > money
totalScore[mask] = -1               # give bad score to configurations that are too expensive

# argmax yields the ID of the best configuration ...
bestID = np.argmax(totalScore)
print(bestID)
print(meshgrid[0].shape)

# ... and unravel_index reconstructs the indices in our multidimensional array from this ID
bestConfig = np.unravel_index(bestID, shape=meshgrid[0].shape)

print(bestConfig)

# Output on screen:
print("Sugar-Strategy:")
print("Sweet                | Count  | Price | Score ")
print("---------------------+--------+-------+-------")
for i in range(N) :
    ithComponentCountCount = meshgrid[i][bestConfig]                            # meshgrid[i] is the i-th tensor, i.e. the one for dark chocolate/milk chocolate/...
                                                                                # bestConfig holds the coordinates of the best configuration as a tuple
                                                                                # thus, meshgrid[i][bestConfig] is the number of bars/packages/... of the i-th sweet you'd want to buy, optimally
    print(f"{names[i]:20} | {ithComponentCountCount:6.0f} | {ithComponentCountCount * prices[i]:5.2f} | {ithComponentCountCount * weights[i]:5}")
print("---------------------+--------+-------+-------")
print(f"{'TOTAL':20} | {np.sum(bestConfig):6} | {totalMoney[bestConfig]:5.2f} | {totalScore[bestConfig]:5.0f}")
print()
print("Analyzed", np.prod(1 + upperLimits, dtype=np.int), "configurations.")
