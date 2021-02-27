import numpy as np
import matplotlib.pyplot as plt

# Generate the finn oscillation ---------------------------------------------------------------------------------------
dt = 0.000001
t = np.arange(0, 0.2, dt)  # seconds: (min, max, step)
frequency_vibration1 = 10  # Vibration frequency 1 [Hz]
frequency_vibration2 = 20  # Vibration frequency 2 [Hz]
vibration1 = np.sin(2*np.pi*frequency_vibration1*t)  # vibration deformation [cm]
vibration2 = np.sin(2*np.pi*frequency_vibration2*t)  # vibration deformation [cm]

# Bragg reflexion based on fin oscillation ----------------------------------------------------------------------------
ratio = 2
bragg_reflected_1530_1 = 1530 + (ratio*vibration1)  # 2nm/cm ^2
bragg_reflected_1530_2 = 1530 + (ratio*vibration2)  # 2nm/cm ^2
bragg_reflected_1550_1 = 1550 + (ratio*vibration1)  # 2nm/cm ^2

# Spectral sweep of the filter ----------------------------------------------------------------------------------------
frequency_sweep = 200
filter_sweep = 1555 + 35*np.sin(2*np.pi*frequency_sweep*t)

# Index of the time when the wavelength cross
intersection_1530_1 = np.argwhere(np.diff(np.sign(bragg_reflected_1530_1 - filter_sweep))).flatten()
intersection_1530_2 = np.argwhere(np.diff(np.sign(bragg_reflected_1530_2 - filter_sweep))).flatten()
intersection_1550_1 = np.argwhere(np.diff(np.sign(bragg_reflected_1550_1 - filter_sweep))).flatten()

# Reference wavelength when the finn doesnt move ---------------------------------------------------------------------
ref_1530 = 1530*np.ones(len(t))
ref_1550 = 1550*np.ones(len(t))

intersection_1530_ref = np.argwhere(np.diff(np.sign(ref_1530 - filter_sweep))).flatten()
intersection_1550_ref = np.argwhere(np.diff(np.sign(ref_1530 - filter_sweep))).flatten()

# Difference between the wl when the FBG and filter cross and the reference wl --------------------------------------
diff_ref_1530_1 = (filter_sweep[intersection_1530_1] - filter_sweep[intersection_1530_ref])/ratio  # (15xx-1530)/2
#               = (filter value of when they actually cross - filter value of when they should cross) / (ratio)
diff_ref_1530_2 = (filter_sweep[intersection_1530_2] - filter_sweep[intersection_1530_ref])/ratio

# Illustration of the difference
plt.figure(1)
plt.plot(t, filter_sweep, label="Filter sweep", color="b")
plt.plot(t, ref_1530, label="Bragg 1530 reflexion at rest", color="g")
plt.scatter(t[intersection_1530_ref], filter_sweep[intersection_1530_ref], s=10, color="g", zorder=5)
plt.xlabel("time [s]")
plt.ylabel("wavelength [nm]")
plt.title("Signal at rest")
plt.ylim(1525, 1535)
plt.legend()

plt.figure(2)
plt.plot(t, filter_sweep, label="Filter sweep", color="b")
plt.plot(t, bragg_reflected_1530_1, label="Bragg 1530 reflexion at f1", color="g")
plt.scatter(t[intersection_1530_1], bragg_reflected_1530_1[intersection_1530_1], s=10, color="g", zorder=5)
plt.xlabel("time [s]")
plt.ylabel("wavelength [nm]")
plt.title("Save wavelength two frequency")
plt.ylim(1525, 1535)
plt.legend()

plt.figure(3)
plt.plot(t, vibration1, label="vibration", color="b")
plt.plot(dt*intersection_1530_1, diff_ref_1530_1, label="signal received", color="y")
plt.xlabel("time [s]")
plt.ylabel("wavelength [nm]")
plt.title("vibration vs signal received")
plt.legend()

plt.show()
