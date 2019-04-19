import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x + b

werte = csv_read("csv/d=2.4cm.csv")
xdata = np.zeros(27)
ydata = np.zeros(27)
dataplotx = np.zeros(9)
dataploty = np.zeros(9)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[1])
        i+=1

#gerade von [18] bis [24]
for i in range(0, 9):
    dataplotx[i] = xdata[i+15]
    dataploty[i] = ydata[i+15]

print(dataplotx[8])

x_line = np.linspace(600, 950)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, dataplotx, dataploty)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(pcov)

plt.xlabel(r"Druck $p$ / mbar")
plt.ylabel(r"Counts")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_countd24.pdf")