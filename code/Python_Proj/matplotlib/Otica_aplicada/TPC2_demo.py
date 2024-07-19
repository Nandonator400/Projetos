import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para entrar no countour
def wave_function(x, z, w, k, t):
    return 1/(x**2 + z**2)**0.5 * np.exp(-1j*k*(x**2+z**2)**0.5)*np.exp(1j*w*t)

# limites para eixos x e z
x = np.linspace(-0.5, 0.5, 50)
z = np.linspace(-0.5, 0.5, 50)

X, Z = np.meshgrid(x, z) # grid 2x2

w = 1
k = 20*3.1415
t = 0

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

Z_real = np.real(wave_function(X, Z, w, k, t )) #parte real da solução
Z_abs = np.abs(wave_function(X, Z, w, k, t )) #parte real da solução

# Create the filled contour plot for the real part of the complex function
contour1 = ax1.contourf(X, Z, Z_real, levels=30, cmap='viridis')
fig.colorbar(contour1, ax=ax1, label='Real Part')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.set_title('Real Part of Complex-valued Function')

# Create the 3D surface plot for the absolute value of the complex function
surf = ax2.plot_surface(X, Z, Z_abs, cmap='hot', edgecolor='none')
fig.colorbar(surf, ax=ax2, label='Absolute Value')
ax2.set_xlabel('X')
ax2.set_ylabel('Z')
ax2.set_zlabel('Absolute Value')
ax2.set_title('Absolute Value of Complex-valued Function')

plt.tight_layout()
plt.show()