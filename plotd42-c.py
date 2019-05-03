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
xdata = np.zeros(17)
ydata = np.zeros(17)
dataplotx = np.zeros(8)
dataploty = np.zeros(8)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0]) * (x_0 / p_0)
        ydata[i] = float(values[1])
        i+=1

#[7] bis [15]
for i in range(0, 8):
    dataplotx[i] = xdata[i+7]
    dataploty[i] = ydata[i+7]


x_line = np.linspace(300, 580) * (x_0 / p_0)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, dataplotx, dataploty)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)             #a_{4,2cm} = (-2,8 \pm 0,2) \cdot 10^{4}
print(np.sqrt(pcov))    #b_{4,2cm} = (6,6 \pm 0,4) \cdot 10^{4}

plt.xlabel(r"Effektive Länge $x$ / cm")
plt.ylabel(r"Gesamtzählrate")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_countd42.pdf")