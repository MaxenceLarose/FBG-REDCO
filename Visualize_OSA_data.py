import logging
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

files = {
    "source": {
        "filepath": "data/SOURCE2.CSV",
        "label": "Source large bande",
        "color": "b"
    },
    "filter_0V": {
        "filepath": "data/0V-100nm-bon.CSV",
        "label": "Filtre avec alimentation de 0V",
        "color": "r"
    },
    "filter_5V": {
        "filepath": "data/5V-100nm.CSV",
        "label": "Filtre avec alimentation de 5V",
        "color": "g"
    }
}

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

for file in files.items():
    key, values = file[0], file[1]
    logging.debug(f"Loading {key}")
    wavelength = np.loadtxt(values["filepath"], usecols=0, delimiter=',', skiprows=34)
    intensity_dB = np.loadtxt(values["filepath"], usecols=1, delimiter=',', skiprows=34)
    line_1, = ax.plot(wavelength, intensity_dB, color=values["color"], linewidth=1.5, label=file[1]["label"])

# ax.set_xscale('log')
ax.set_title("Courbe OSA", fontsize=14)
ax.set_xlabel("Longueur d'onde [nm]", fontsize=18)
ax.set_xlim([1530, 1580])
ax.set_ylim([-100, -25])
ax.set_ylabel("Intensité [dB]", fontsize=18)
ax.legend(fontsize=14)
ax.minorticks_on()

# plt.grid()
fig.set_size_inches(12, 7)
fig.savefig('Figs/Courbe_OSA.pdf', bbox_inches = 'tight', dpi=600)
plt.show()
