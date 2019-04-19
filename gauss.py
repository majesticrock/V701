import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

werte = csv_read("csv/100messungen.csv")

data = np.zeros(100)

i=0
for values in werte:
    data[i] = float(values[0])
    i+=1

minimum = np.amin(data)
maximum = np.amax(data)

print(minimum)
print(maximum)


n = 12
bins = np.zeros(n)
size = 52#(maximum-minimum)/n
print(size)

for c in data:
    m = c
    i = 0
    while (m >= (minimum+size)):
        i+=1
        m -= size
    
    bins[i-1]+=1

xline = np.linspace(0,n,n)
plt.bar(xline, bins, width=0.8, align="center", label="Messwerte")

plt.xlabel(r"Counts")
plt.ylabel(r"Häufigkeit")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_gauss.pdf")