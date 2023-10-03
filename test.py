import numpy as np
import matplotlib.pyplot as plt

g = 9.8


u = 420  # initial velocity (m/s)
theta = 45  # angle (deg)
theta = np.deg2rad(theta)

t_flight = 2 * u * np.sin(theta) / g
t = np.linspace(0, t_flight, 100)
x = u * np.cos(theta) * t
y = u * np.sin(theta) * t - 0.5 * g * t**2

fig, ax = plt.subplots()
ax.plot(x, y, color="k")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
