import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.signal import find_peaks, peak_widths

def wave_function(x, z, w, k): # Função para entrar no countour w = z0
    return 1/(z + 1j*w) * np.exp(-1j*k*(x**2)/(2*(z + 1j*w))) * np.exp(-1j*k*z)

xlim = 2.5
ylim = 1.0
const = 200.0

x = np.linspace(-xlim, xlim, int(xlim*const)) # limites para eixos x e z 
z = np.linspace(-ylim, ylim, int(ylim*const))

X, Z = np.meshgrid(x, z) # grid 2x2

w = 1.2 #z0
k = 10*pi

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4, projection='3d')

Z_intensity = (np.abs((wave_function(Z, X, w, k))))**2#intensidade
Z_phase = np.abs(np.angle(wave_function(Z, X, w, k))) #fase
Z_real_abs = (np.abs(np.real(wave_function(Z, X, w, k))))**2#intensidade real

contour1 = ax1.contourf(X, Z, Z_intensity, levels=50, cmap='jet') # plots de 1 a 4
fig.colorbar(contour1, ax=ax1, label='Intensity')
ax1.set_xlabel('Z')
ax1.set_ylabel('X')
ax1.set_title('Intensity of Gaussian Beam')

contour2 = ax2.contourf(X, Z, Z_phase, levels=50, cmap='jet')
fig.colorbar(contour2, ax=ax2, label='Phase')
ax1.set_xlabel('Z')
ax1.set_ylabel('X')
ax2.set_title('Phase of Gaussian Beam')

contour3 = ax3.contourf(X, Z, Z_real_abs, levels=50, cmap='jet')
fig.colorbar(contour3, ax=ax3, label='Intensity of real part')
ax1.set_xlabel('Z')
ax1.set_ylabel('X')
ax3.set_title('Intensity of real part')

contour4 = ax4.plot_surface(X, Z, Z_intensity, cmap='jet', edgecolor='none')
fig.colorbar(contour4, ax=ax4, label='Intensity')
ax1.set_xlabel('Z')
ax1.set_ylabel('X')
ax4.set_title('3D Intensity of Gaussian Beam')
plt.tight_layout() 
plt.show()

# Determinar a largura a meia altura 
x0_index = np.argmin(np.abs(x)) # valor mais próximo de 0
Z_intensity_x0 = Z_intensity[:, x0_index]
xw_index = np.argmin(np.abs(x - w)) # valor mais próximo de w
Z_intensity_xw = Z_intensity[:, xw_index]

peaks0, _ = find_peaks(Z_intensity_x0) # encontra os picos locais
peaksw, _ =  find_peaks(Z_intensity_xw)

results_half0 = peak_widths(Z_intensity_x0, peaks0, rel_height=0.5)
results_halfw = peak_widths(Z_intensity_xw, peaksw, rel_height=0.5)  

fwhm_z0 = results_half0[0][int((len(peaks0)-1)/2.0)]/100.0 # escolhe o pico médio
fwhm_zz0 = results_halfw[0][int((len(peaksw)-1)/2.0)]/100.0 # a função é simétrica 

plt.figure(figsize=(10, 6))
plt.plot(z, Z_intensity_x0, label='Intensity at z=0')
plt.plot(z, Z_intensity_xw, label='Intensity at z=z0')
plt.axhline(np.max(Z_intensity_x0) / 2, color='r', linestyle='--', label='Half Maximum z = 0')
plt.axhline(np.max(Z_intensity_xw) / 2, color='g', linestyle='--', label='Half Maximum z = z0')
plt.xlabel('Z')
plt.text(z[len(z)//2], np.max(Z_intensity_x0) / 2, f'FWHM, z=0: {fwhm_z0:.5f}', color='r', va='bottom', ha='left')
plt.text(z[len(z)//2], np.max(Z_intensity_xw) / 2, f'FWHM, z=z0: {fwhm_zz0:.5f}', color='g', va='top', ha='left')
plt.ylabel('Intensity') 
plt.legend()
plt.grid(True)
plt.show()