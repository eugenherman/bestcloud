import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp


def asteroid_mass(radius_km, density_g_per_cm3):
    radius_m = radius_km * 1000  # Convert km to meters
    density_kg_per_m3 = density_g_per_cm3 * 1000  # Convert g/cm³ to kg/m³
    volume = (4/3) * np.pi * radius_m**3  # Volume of a sphere
    mass = volume * density_kg_per_m3  # Mass calculation
    return mass

def gravitational_force(m1, m2, distance_m):
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    return G * (m1 * m2) / distance_m**2

# Given data
radius1_km = 100
density1_g_per_cm3 = 5  # Assuming 'tramp' means 'grams'

radius2_km = 200
density2_g_per_cm3 = 8

distance_km = 1000  # Assume a distance of 1000 km between their centers
distance_m = distance_km * 1000  # Convert km to meters

# Calculate masses
mass1 = asteroid_mass(radius1_km, density1_g_per_cm3)
mass2 = asteroid_mass(radius2_km, density2_g_per_cm3)

# Calculate gravitational force
force = gravitational_force(mass1, mass2, distance_m)

print(f"Gravitational Force between the asteroids: {force:.2e} N")

# Visualization
fig, ax = plt.subplots()
ax.set_xlim(-distance_km/2, distance_km/2)
ax.set_ylim(-radius2_km, radius2_km)
ax.set_aspect('equal')

# Draw asteroids
asteroid1 = plt.Circle((-distance_km/2, 0), radius1_km, color='blue', label='Asteroid 1')
asteroid2 = plt.Circle((distance_km/2, 0), radius2_km, color='red', label='Asteroid 2')
ax.add_patch(asteroid1)
ax.add_patch(asteroid2)

# Draw force vector
ax.annotate('', xy=(distance_km/2 - radius2_km, 0), xytext=(-distance_km/2 + radius1_km, 0),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
ax.text(0, 10, f'F = {force:.2e} N', ha='center', fontsize=12, color='black')

# Labels and show plot
ax.set_xlabel('Distance (km)')
ax.set_ylabel('Position (km)')
ax.legend()
plt.title("Gravitational Attraction Between Two Asteroids")
plt.show()
