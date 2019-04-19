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

x_0 = 4.2 #cm
p_0 = 1000 #mbar

werte = csv_read("csv/d=4.2cm.csv")
xdata = np.zeros(16)
ydata = np.zeros(16)
dataplotx = np.zeros(11)
dataploty = np.zeros(11)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        if(i < 16):
            xdata[i] = float(values[0]) * (x_0 / p_0)
            ydata[i] = float(values[3])
        i+=1

for i in range(0, 11):
    dataplotx[i] = xdata[i]
    dataploty[i] = ydata[i]


x_line = np.linspace(0, 475) * (x_0 / p_0)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, dataplotx, dataploty)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(pcov))

plt.xlabel(r"Effektive Länge $x$ / cm")
plt.ylabel(r"Energie $E$ / MeV")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_E42.pdf")