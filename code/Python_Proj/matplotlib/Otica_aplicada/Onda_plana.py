import numpy as np
import matplotlib.pyplot as plt

# Função para entrar no countour
def wave_function_plana(z, x, k, a ):
    return a * np.exp(-1j*k*z)

def wave_function(z, x, k, a , theta):
    return a * np.exp(-1j*k*z*np.sin(theta) -1j*k*x*np.cos(theta))

# limites para eixos x e z
x = np.linspace(-0.5, 0.5, 50)
z = np.linspace(-0.5, 0.5, 50)

X, Z = np.meshgrid(x, z) # grid 2x2

a = 1
k = 20*3.1415
theta = 10

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Calculate real part of wave function for tilted wave
Z_real = np.real(wave_function(Z, X, k, a, theta))
Z_real2 = np.real(wave_function_plana(Z, X, k, a))

contour1 = ax1.contourf(X, Z, Z_real, levels=30, cmap='viridis')
fig.colorbar(contour1, ax=ax1, label='Real Part')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.set_title('Tilted Wave Function')

# Plot contour plot for untilted wave
contour2 = ax2.contourf(X, Z, Z_real2, levels=30, cmap='viridis')
fig.colorbar(contour2, ax=ax2, label='Real Part')
ax2.set_xlabel('X')
ax2.set_ylabel('Z')
ax2.set_title('Untilted Wave Function')

plt.tight_layout()
plt.show()
