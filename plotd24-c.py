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

x_0 = 2.4 #cm
p_0 = 1000 #mbar

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
        xdata[i] = float(values[0]) * (x_0 / p_0)
        ydata[i] = float(values[1])
        i+=1

#gerade von [15] bis [24]
for i in range(0, 9):
    dataplotx[i] = xdata[i+15]
    dataploty[i] = ydata[i+15]

x_line = np.linspace(600, 950) * (x_0 / p_0)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, dataplotx, dataploty)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)             #a_{2,4cm} = (-9,0 \pm 0,6) \cdot 10^{4}
print(np.sqrt(pcov))    #b_{2,4cm} = (2,0 \pm 0,1) \cdot 10^{5} 

plt.xlabel(r"Effektive Länge $x$ / cm")
plt.ylabel(r"Gesamtzählrate")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_countd24.pdf")