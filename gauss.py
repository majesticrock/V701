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
print(size)

for c in data:
    m = c
    i = 0
    while (m >= (minimum+size)):
        i+=1
        m -= size
    
    bins[i-1]+=1

#verteilung
#erwartungswert mu = sum(x_i * p_i) x_i = werte, p_i = wahrsch. pro wert
mu = 0
for x_i in data:
    mu += (x_i * (1/100))

#Varianz sigma^2 = sum((x_i - mu)^2 * p_i)
sigma2 = 0
for x_i in data:
    sigma2 += ((x_i - mu)**2 * (1/100))

print(mu)
print(sigma2)

#Normierungsfaktor der Gaußkurve entfernen
#multipliziere mit höchstem bin
scale = np.sqrt(2*np.pi*sigma2) * np.amax(bins)

xline = (np.linspace(0,n-1,n) + 0.5) * size + minimum
plt.bar(xline, bins, width=0.75*size, align="center", label="Messwerte")

xgauss = np.linspace(minimum, maximum)

labelGauss = np.linspace(0,n) * size + minimum
plt.plot(labelGauss, scale * gaussVerteilung(xgauss, mu, sigma2), "r-",label="Theoriekurve")

plt.xlabel(r"Counts")
plt.ylabel(r"Häufigkeit")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot_gauss.pdf")