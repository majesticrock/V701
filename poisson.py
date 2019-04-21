import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def gaussVerteilung(x, mu, sigma2):
    return ((1/np.sqrt(2*np.pi*sigma2)) * np.e**(- (x - mu)**2/(2*sigma2) ))

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


xline = np.linspace(0,n,n) * size + minimum
plt.bar(xline, bins, width=size, align="center", label="Messwerte")


plt.xlabel(r"Counts")
plt.ylabel(r"Häufigkeit")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_gauss.pdf")