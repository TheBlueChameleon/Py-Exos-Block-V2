import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import csv
import math
import random

# ============================================================================ #
# problem 4

# ............................................................................ #
# read data

with open("transition-probabilties.txt", "r") as handle :
  rdr = csv.reader(handle, delimiter="\t")
  
  # skip header line:
  line = next(rdr)                                # read first line
  while True :
    if len(line) == 0 :                           # skip empty lines
      line = next(rdr)
      continue
    
    if line[0].startswith("incoming") :           # we've found the data section when we hit the line starting with "incoming"
      headsX = line[1:]                           # save the column heads, excluding the "incomping/..." string
      break
    
    line = next(rdr)
  
  # read data section 1
  headsY = []                                     # line heads of the first data section
  data1  = []                                     # actual data
  for line in rdr :
    if len(line) == 0 : break
    
    headsY.append(line[0])
    data1.append(line[1:])
  
  # skip header data in section 2: copy and paste
  line = next(rdr)                                # skip first line
  while True :
    if len(line) == 0 :                           # skip empty lines
      line = next(rdr)
      continue
    
    if line[0].startswith("incoming") :           # up to the point where "incoming" marks the data section
      break
    
    line = next(rdr)
  
  data2 = []
  for line in rdr :
    if not len(line) : break
    data2.append(float(line[1]))
    
  
# convert text to numbers
for i, line in enumerate(data1) :
  data1[i] = [float(datapoint) for datapoint in line]

# ............................................................................ #
# simple plot

fig1 = plt.figure()
gs = fig1.add_gridspec(1,4)

matView = fig1.add_subplot(gs[:3])
barView = fig1.add_subplot(gs[3:], sharey=matView)

col = matView.pcolor(data1)

barView.barh(range(len(data2)), data2)

fig1.suptitle("Transmission Experiment")
fig1.colorbar(col)
matView.set_title("Transmssions")
matView.set_xlabel("Outgoing configuration ID")
matView.set_ylabel("Incoming configuration ID")

barView.set_title("Test Sum")

fig1.show()

# ............................................................................ #
# complete plot

tickerX = lambda x, i : headsX[int(x)] if x < len(headsX) else f"{x:2.0f}"
tickerY = lambda y, i : headsY[int(y)] if y < len(headsY) else f"{y:2.0f}"

formatterX = FuncFormatter(tickerX)
formatterY = FuncFormatter(tickerY)

fig2 = plt.figure()
gs = fig2.add_gridspec(1,4)

matView = fig2.add_subplot(gs[:3])
barView = fig2.add_subplot(gs[3:], sharey=matView)

matView.xaxis.set_major_formatter(formatterX)
matView.yaxis.set_major_formatter(formatterY)

col = matView.pcolor(data1)
barView.barh(headsY, data2)
barView.yaxis.set_visible(False)

fig2.suptitle("Transmission Experiment")
fig2.colorbar(col)
matView.set_title("Transmssions")
matView.set_xlabel("Outgoing configuration")
matView.set_ylabel("Incoming configuration")

barView.set_title("Test Sum")

fig2.show()

input("Please press Enter to continue")
plt.close(fig1)
plt.close(fig2)

# ============================================================================ #
# problem 3

shots = 300
sigma = 10

phi = [random.uniform(0, math.tau) for _ in range(shots)]         # tau = 2 * pi
r   = [abs(random.gauss(0, sigma)) for _ in range(shots)]

fig = plt.figure()
drw = fig.add_subplot(projection="polar")
drw.set_ylim(0, 50)
drw.scatter(phi, r, marker = "x")

fig.show()
input("Please press Enter to continue")
plt.close(fig)

# ============================================================================ #
# problem 2

# ............................................................................ #
# common code elements for both, simple and full version:

Xmin = -math.pi
Xmax = +math.pi
Ymin = -5
Ymax = +5
resolution = 100

ticker = lambda x, i : f"{x / math.pi:4.2f}$\pi$"
formatter = FuncFormatter(ticker)

X = [x / resolution for x in range(int(Xmin * resolution), int(Xmax * resolution))]
Y = [math.tan(x) for x in X]

xTicks = [i / 4 * math.pi for i in range(-4, 5)]

# ............................................................................ #
# simple form

fig1 = plt.figure()
drw = fig1.add_subplot(111)

null = [0] * len(X)

drw.plot(X, Y, "-")
drw.plot(X, null, "k,")

drw.set_title ("Herzschlag")
drw.set_xlabel("Winkel")
drw.set_ylabel("Steigung")

drw.set_ylim(Ymin, Ymax)
drw.set_xticks(xTicks)
drw.xaxis.set_major_formatter(formatter)

fig1.show()

# ............................................................................ #
# full form with no vertical lines at the poles and coordinate cross

fig2 = plt.figure()
drw = fig2.add_subplot(111)

# find spots where the sign of the plot changes (poles):
splitPoints = [0]
lastSign = Y[0] > 0
for i, y in enumerate(Y) :
    if (y > 0) != lastSign :
        lastSign = (y > 0)
        splitPoints.append(i)
splitPoints.append(len(Y))

# and plot section by section:
for i in range(len(splitPoints) - 1) :
    start = splitPoints[  i  ]
    stop  = splitPoints[i + 1]
    
    drw.plot(X[start : stop], Y[start : stop], color="steelblue")

# coordinate cross -- your search engine of choice will find them easily
drw.hlines(0, Xmin, Xmax)
drw.vlines(0, Ymin, Ymax)

# same as before
drw.set_title ("Herzschlag")
drw.set_xlabel("Winkel")
drw.set_ylabel("Steigung")

drw.set_ylim(Ymin, Ymax)
drw.set_xticks(xTicks)
drw.xaxis.set_major_formatter(formatter)

fig2.show()

input("Please press Enter to continue")
plt.close(fig1)
plt.close(fig2)

# ............................................................................ #
# the heart

fig3 = plt.figure()
drw = fig3.add_subplot(111, projection="polar")

#https://pavpanchekha.com/blog/heart-polar-coordinates.html
heart = lambda t : (math.sin(t) * math.sqrt( abs(math.cos(t)) )) / (math.sin(t) + 7/5) - 2 * math.sin(t) + 2

# another form for the heart can be found here: https://www.pinterest.de/pin/863987509751007911/
#heart = lambda theta : 3.5 - 1.5 * abs(math.cos(theta)) * math.sqrt(1.3 + abs(math.sin(theta))) + math.cos(2 * theta) - 3 * math.sin(theta) + 0.7 * math.cos(12.2 * theta)

resolution = 100
Theta = [t / resolution for t in range(int(2 * resolution * math.pi))]
R = [heart(theta) for theta in Theta]

drw.plot(Theta, R, "r")
fig3.show()

input("Please press Enter to continue")
plt.close(fig3)

# ============================================================================ #
# problem 1

class SpectrumPlot :
    def __init__(self, filename = None) :
        self.fig = plt.figure(figsize=(15,5))
        self.drw = self.fig.add_subplot(111)
        
        self.wavenumbers = []
        self.intensities = []
        self.minima      = []
        
        self.supTitle    = "IR Spectrum"
        self.title       = ""
        
        self.xlabel = "wavenumber (cm$^{-1})$"
        self.ylabel = "reflectance"
        
        self.linetype = "r-"
        
        self.minWidth = 7
        self.minValBaseline = 0.4
        self.minOverlapWidth = 400
        
        self.plotsReady  = False
        
        if filename : self.loadFile(filename)
    
    # ........................................................................ #
    
    def loadFile(self, filename) :
        self.wavenumbers = []
        self.intensities = []
        self.plotsReady  = False
        
        # Einlesen
        with open(filename, "r") as handle :
            rdr = csv.reader(handle, delimiter=" ")
            
            for line in rdr :
                if line[0].startswith('##TITLE') : self.title=line[0][8:]
                if line[0].startswith('##END=')  : break
                if line[0].startswith('#')       : continue
                
                self.wavenumbers.append( float(line[0]) )
                self.intensities.append( float(line[1]) )
        
        # Normalisieren
        factor = 1 / max(self.intensities)
        for i, intensity in enumerate(self.intensities) :
            self.intensities[i] *= factor
        
        self.findMinima()
        
    # ........................................................................ #
    
    def findMinima(self) :
        self.minima = []
        
        for i, v in enumerate(self.intensities) :
            # we regard data points within +/- self.minWidth from point i.
            # These points need to exist in the first place:
            if i < self.minWidth or i > len(self.intensities) - self.minWidth :
                continue
            
            # exclude completely flat sections from our analysis
            if min(self.intensities[i-self.minWidth:i+self.minWidth]) == max(self.intensities[i-self.minWidth:i+self.minWidth]) :
                continue
            
            # v is a local minimum if it is the smallest value in the window:
            if v == min(self.intensities[i-self.minWidth:i+self.minWidth]) :
                # store index and value of the minimum. From these we can get
                # x- and y-value which we need for the arrows
                self.minima.append(i)
            
            # another approach:
            # v will be accepted as a local minimum if:
            # a) the sign of the slope to the left and to the right changes,
            # i.e.:
            #    intensities[i - 1] > v and intensities[i + 1] > v
            # b) the distance v to <maximum of a window around v> is bigger than
            #    some threshold, i.e.:
            #    max(intensities[i - minWidth : i + minWidth]) - v > threshold
            # 
            # You might have found different, reasonable solutions to this.
        
    # ........................................................................ #
    
    def preparePlot(self) :
        if len(self.wavenumbers) == 0 : raise RuntimeError("No data in the plot")
        
        self.fig.suptitle(self.supTitle)
        self.drw.set_title(self.title)
        
        self.drw.plot(self.wavenumbers, self.intensities, self.linetype)
        
        # X-Achse absteigend laufen lassen:
        wn_max = max(self.wavenumbers)
        wn_min = min(self.wavenumbers)
        self.drw.set_xlim(wn_max, wn_min)
        
        self.drw.set_xlabel(self.xlabel)
        self.drw.set_ylabel(self.ylabel)
        
        yOff = self.minValBaseline
        for i, thisMinIdx in enumerate(self.minima) :
            if i > 0 :
                lastMinIdx = self.minima[i - 1]
                
                if self.wavenumbers[lastMinIdx] - self.wavenumbers[thisMinIdx] < self.minOverlapWidth :
                    yOff += 0.05
                    if yOff > 0.95 : yOff = self.minValBaseline
                else :
                    yOff  = self.minValBaseline
            
            self.drw.annotate(
                str(self.wavenumbers[thisMinIdx]),
                xy = (self.wavenumbers[thisMinIdx], self.intensities[thisMinIdx]),
                xytext = (self.wavenumbers[thisMinIdx] + .1, yOff),
                arrowprops = {
                    'color'      : 'grey',
                    'headwidth'  : 5,
                    'headlength' : 5,
                    'width'      : .1
                },
                horizontalalignment = 'center'
            )
        
        self.plotsReady = True
    
    # ........................................................................ #
    
    def show(self) :
        if not self.plotsReady : self.preparePlot()
        self.fig.show()
    
    # ........................................................................ #
    

caffeine = SpectrumPlot("caffeine.jdx")
caffeine.show()

ethanol =  SpectrumPlot("ethanol.jdx")
ethanol.supTitle = "IR Gas Phase Spectrum"
ethanol.ylabel = "transmittivity"
ethanol.linetype = "b:"
ethanol.show()

input("Please press Enter to quit")
