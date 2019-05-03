import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def factorial(k):
    if(k > 0):
        return k*factorial(k-1)
    else:
        return 1

def poissonVerteilung(k, kFact, lam):
    return ((lam**k)/kFact) * np.e**(-lam)

werte = csv_read("csv/100messungen.csv")

data = np.zeros(100)

i=0
for values in werte:
    data[i] = float(values[0])
    i+=1

minimum = np.amin(data)
maximum = np.amax(data)

n = 9
bins = np.zeros(n)
size = (maximum-minimum)/n

for c in data:
    m = c
    i = 0
    while (m >= (minimum+size)):
        i+=1
        m -= size
    
    bins[i-1]+=1

#Verteilung
lam = 0
for x_i in data:
    lam += 1/100 * (x_i-minimum) * 1/size

print(lam)

xline = np.linspace(0,n-1,n)
plt.bar(xline, bins/100, width=0.8, align="center", label="Messwerte")

xlineFact = np.zeros(n)
for i in range(0, n):
    xlineFact[i] = factorial(i)

scale=np.amax(bins)/np.amax(poissonVerteilung(xline, xlineFact, lam))

labelPoisson = xline
plt.bar(xline, poissonVerteilung(xline, xlineFact, lam), color="r", width=(0.4), align="center", label="Theoriekurve")

print(xlineFact)
print(poissonVerteilung(xline, xlineFact, lam))

plt.xlabel(r"Bin Nummer")
plt.ylabel(r"Wahrscheinlichkeit")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_poisson.pdf")