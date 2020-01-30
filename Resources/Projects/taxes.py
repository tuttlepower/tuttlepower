import numpy as np
np.linspace
import matplotlib.pyplot as plt

x = []

income = []

taxes = []

y=0

while y < 1000000:
    x.append(y)
    income.append(y)
    if y >= 0 and y<=9700:
        taxes.append(0)
    if y > 9700 and y<=39475:
        taxes.append(970)
    if y > 39475 and y<=84200:
        taxes.append(4543.00)
    if y > 84200 and y<=160725:
        taxes.append(14382.50)
    if y > 160725 and y<=204100:
        taxes.append(32748.50)
    if y > 204100 and y<=510300:
        taxes.append(46628.50)
    if y > 510300:
        taxes.append(153798.50)

    y=y+1

y = np.vstack([income,taxes])

labels = ["Income ", "Taxes",]

fig, ax = plt.subplots()
ax.stackplot(x, income,taxes, labels=labels)
ax.legend(loc='upper left')
ax.grid(True)
plt.show()
