import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from PIL import Image

wavelength = 632.8*10**(-9) #Comprimento de onda da luz em m

f= (25+5*np.sin(106716- 100000))/100 # Distância focal em [m] das duas lentes no sistema 4f

system_size, laser_size= 0.01, 0.008 # Dimensão dos objetos em [m]

filter_size_low, filter_size_high = 0.001, 0.002 # Dimensões em [m] das aberturas a ser usadas para cada filtro

filter="low" # Defenir modo de operacão do filtro como "high", "low" ou "none"

low_max = filter_size_low/(2*wavelength*f) # calcular a frequência máxima do filtro passa baixo
high_min = filter_size_high/(2*wavelength*f) # calcular a frequência mínima do filtro passa alto

print("Frequency: ",f)
print("Low-filter max frequency: ", low_max)
print("High-filter minfrequency: ", high_min)

N_mask, N_output = 1024, 1024 # Número de píxeis a usar para criar a grid 2x2
pixsize_mask = system_size / N_mask # tamanho de um pixel

#######

x = np.linspace(-system_size / 2, system_size / 2, num=N_mask)
y = np.linspace(-system_size / 2, system_size / 2, num=N_mask)
xx, yy = np.meshgrid(x, y) # Criação da grid 

# Frequências x e y são os ranges de frequência a ser representados no plano de fourier a uma distância f da primeira lente
# Objeto em z = 0, primeira lente em z = f e plano de fourier em z = 2f

freq_x = fftpack.fftshift(fftpack.fftfreq(N_mask, d=pixsize_mask))
freq_y = fftpack.fftshift(fftpack.fftfreq(N_mask, d=pixsize_mask))

x_freq=freq_x*wavelength*f # mapeamento das coordenadas no plano focal da lente
y_freq=freq_y*wavelength*f
xx_freq, yy_freq = np.meshgrid(x_freq, y_freq)

input_field = np.zeros((N_mask, N_mask)) # Campo laser monocromático com abertura circular
input_field[np.sqrt(xx**2+yy**2) < laser_size/2] = 1

# Campo de input em metros
plt.imshow(input_field, extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title("Laser Intensity")
plt.show()

# Objeto escolhido para fazer a fft. Fica em z = 0
mypath='C:/Users/Luis/Desktop/Python_Proj/matplotlib/Otica_aplicada/imagemfft.jpg'

img = Image.open(mypath) # Carregar imagem
img = img.convert('L') # Converter para preto e branco
img = img.resize((len(x), len(y))) # Reconverter a imagem para o tamanho escolhido (N_mask e N_output)
img_array = np.asarray(img) #Converter imagem para um array 2x2
object_ = img_array / 255.0 # Normalizar a imagem

filter_low = np.zeros((N_mask, N_mask)) # Filtro passa baixo
filter_low[np.sqrt(xx_freq**2+yy_freq**2) < filter_size_low/2] = 1

filter_high = np.ones((N_mask, N_mask)) # Filtro passa alto
filter_high[np.sqrt(xx_freq**2+yy_freq**2) < (filter_size_high/2)] = 0

#######

input_field=input_field*object_

# Mostrar campo de input 
plt.imshow(input_field, extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title("Laser Intensity after object")
plt.show()

fourier_plane = fftpack.fftshift(fftpack.fft2(fftpack.ifftshift(input_field))) # Aplicaçáo da fft 

#Escolha do filtro no plano de Fourier
if filter=="low":
    output_ft = fourier_plane*filter_low
elif filter=="high":
    output_ft = fourier_plane*filter_high
elif filter=="none":
    output_ft = fourier_plane
else:
    print("Error: filter not defined, you can choose none")

#Intensidade no plano de fourier da segunda lente, depois do shift
output_field = fftpack.ifftshift(fftpack.ifft2(fftpack.fftshift(output_ft)))

############

fig, axs = plt.subplots(2,2, figsize=(12,10)) # Definir tela para plot
fig.suptitle('Fourier optics')
axs[0,0].set_title('Input Field') # Plot do campo de input
im_1=axs[0,0].imshow(input_field, extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
axs[0,0].set_xlabel('x (m)')
axs[0,0].set_ylabel('y (m)')

axs[0,1].set_title('Fourier Transform') # Plot da fft
axs[0,1].set_xlabel(r'$f_x$ ($m^{-1}$)')
axs[0,1].set_ylabel(r'$f_y$ ($m^{-1}$)')
im_2=axs[0,1].imshow(np.abs(fourier_plane), extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
if filter=="low":
    axs[1,0].set_title('Fourier Transform with filter') # Plot Da fft com filtro passa baixo
    im_3=axs[1,0].imshow(np.abs(fourier_plane)*filter_low, extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
    axs[1,0].set_xlabel(r'$f_x$ ($m^{-1}$)')
    axs[1,0].set_ylabel(r'$f_y$ ($m^{-1}$)')
elif filter=="high":
    axs[1,0].set_title('Fourier Transform with filter') # Plot Da fft com filtro passa alto
    im_3=axs[1,0].imshow(np.abs(fourier_plane)*filter_high, extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
    axs[1,0].set_xlabel(r'$f_x$ ($m^{-1}$)')
    axs[1,0].set_ylabel(r'$f_y$ ($m^{-1}$)')
elif filter=="none":
    axs[1,0].set_title('Fourier Transform without filter') # Plot Da fft sem filtro
    im_3=axs[1,0].imshow(np.abs(fourier_plane), extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
    axs[1,0].set_xlabel(r'$f_x$ ($m^{-1}$)')
    axs[1,0].set_ylabel(r'$f_y$ ($m^{-1}$)')
else:
    print("Error: filter not defined, you can choose none")
axs[1,1].set_title('Output Field') # Plot da imagem de output
im_4=axs[1,1].imshow(np.abs(output_field), extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
axs[1,1].set_xlabel('x (m)')
axs[1,1].set_ylabel('y (m)')
im_2.set_clim(0, 700)
im_3.set_clim(0, 700)
plt.subplots_adjust(left=0.085, bottom=0.068, right=0.93, top=0.88, wspace=0.486, hspace=0.245)
plt.show()