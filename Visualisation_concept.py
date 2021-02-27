import numpy as np
import matplotlib.pyplot as plt

# Generate the finn oscillation ---------------------------------------------------------------------------------------
dt = 0.0001
t = np.arange(0, 0.2, dt)  # seconds: (min, max, step)
frequency_vibration1 = 10  # Vibration frequency 1 [Hz]
frequency_vibration2 = 20  # Vibration frequency 2 [Hz]
vibration1 = np.sin(2*np.pi*frequency_vibration1*t)  # vibration deformation [cm]
vibration2 = np.sin(2*np.pi*frequency_vibration2*t)  # vibration deformation [cm]

# Bragg reflexion based on fin oscillation ----------------------------------------------------------------------------
bragg_reflected_1530_1 = 1530 + (2*vibration1)  # 2nm/cm ^2
bragg_reflected_1530_2 = 1530 + (2*vibration2)  # 2nm/cm ^2
bragg_reflected_1550_1 = 1550 + (2*vibration1)  # 2nm/cm ^2

# Spectral sweep of the filter ----------------------------------------------------------------------------------------
frequency_sweep = 100
filter_sweep = 1555 + 35*np.sin(2*np.pi*frequency_sweep*t)

# Index of the time when the wavelength cross -------------------------------------------------------------------------
intersection_1530_1 = np.argwhere(np.diff(np.sign(bragg_reflected_1530_1 - filter_sweep))).flatten()
intersection_1530_2 = np.argwhere(np.diff(np.sign(bragg_reflected_1530_2 - filter_sweep))).flatten()
intersection_1550_1 = np.argwhere(np.diff(np.sign(bragg_reflected_1550_1 - filter_sweep))).flatten()

# Illustrations -------------------------------------------------------------------------------------------------------
plt.figure(1)
plt.plot(t, vibration1)
plt.plot(t, vibration2)
plt.xlabel("time [s]")
plt.ylabel("flexion [cm]")
plt.title("Flexion of the fin in time")

plt.figure(2)
plt.plot(t, filter_sweep, label="Filter swept wl at fs")
plt.plot(t, bragg_reflected_1530_1, label="Bragg 1530 reflected wl at f1", color="g")
plt.plot(t, bragg_reflected_1530_2, label="Bragg 1530 reflected wl at f2", color="r")
plt.scatter(t[intersection_1530_1], bragg_reflected_1530_1[intersection_1530_1], s=10, color="g", zorder=5)
plt.scatter(t[intersection_1530_2], bragg_reflected_1530_2[intersection_1530_2], s=10, color="r", zorder=5)
plt.xlabel("time [s]")
plt.ylabel("wavelength [nm]")
plt.title("Save wavelength two frequency")
plt.ylim(1525, 1535)
plt.legend()

plt.figure(3)
plt.plot(t, filter_sweep, label="Filter swept wl at fs")
plt.plot(t, bragg_reflected_1530_1, label="Bragg 1530 reflected wl at f1", color="g")
plt.plot(t, bragg_reflected_1550_1, label="Bragg 1550 reflected wl at f2", color="r")
plt.scatter(t[intersection_1530_1], bragg_reflected_1530_1[intersection_1530_1], s=10, color="g", zorder=5)
plt.scatter(t[intersection_1550_1], bragg_reflected_1550_1[intersection_1550_1], s=10, color="r", zorder=5)
plt.xlabel("time [s]")
plt.ylabel("wavelength [nm]")
plt.title("Two different wavelength")
plt.ylim(1525, 1555)
plt.legend()

# plt.figure(4)
# a = intersection_1530_1 - intersection_1530_2
# plt.plot(a)

plt.show()

