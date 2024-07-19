import numpy as np
import matplotlib.pyplot as plt
from math import pi

def wave_function(x, z, w, k): # Função para entrar no countour w = z0
    return 1/(z + 1j*w) * np.exp(-1j*k*(x**2)/(2*(z + 1j*w))) * np.exp(-1j*k*z)

x = np.linspace(-5, 5, 500) # limites para eixos x e z 
z = np.linspace(-2, 2, 200)

X, Z = np.meshgrid(x, z) # grid 2x2

w = 1.5 #z0
k = 20*pi

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4, projection='3d')

Z_intensity = (np.abs(np.real(wave_function(Z, X, w, k))))**2#intensidade
Z_phase = np.abs(np.angle(wave_function(Z, X, w, k))) #fase
Z_real_abs = np.abs(np.real(wave_function(Z, X, w, k))) #múdulo da parte real

contour1 = ax1.contourf(X, Z, Z_intensity, levels=50, cmap='jet') # plots de 1 a 4
fig.colorbar(contour1, ax=ax1, label='Intensity')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.set_title('Intensity of Gaussian Beam')

contour2 = ax2.contourf(X, Z, Z_phase, levels=50, cmap='jet')
fig.colorbar(contour2, ax=ax2, label='Phase')
ax2.set_xlabel('X')
ax2.set_ylabel('Z')
ax2.set_title('Phase of Gaussian Beam')

contour3 = ax3.contourf(X, Z, Z_real_abs, levels=50, cmap='jet')
fig.colorbar(contour3, ax=ax3, label='Modulus of real part')
ax3.set_xlabel('X')
ax3.set_ylabel('Z')
ax3.set_title('Modulus of real part of Gaussian Beam')

contour4 = ax4.plot_surface(X, Z, Z_intensity, cmap='jet', edgecolor='none')
fig.colorbar(contour4, ax=ax4, label='Intensity')
ax4.set_xlabel('X')
ax4.set_ylabel('Z')
ax4.set_title('Intensity of Gaussian Beam')
plt.tight_layout() 
plt.show()