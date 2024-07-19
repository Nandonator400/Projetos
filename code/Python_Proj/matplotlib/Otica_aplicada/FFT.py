from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Define parameters
wavelength = 546.074*10**(-9) # m

# define the f of the two lenses in the 4f system
f= -1/1212 # in [cm] the focal length of the lens
print("Distância focal f [cm] =", f)

system_size, laser_size= 0.01, 0.15 # in [m] the typical dimensions of the objects
#we are imaging, < 1 cm: paraxial approximation

#these are the two filters we have available to place in the focal plane
filter_size_low, filter_size_high = 0.001, 0.002 #m (one 1 mm aperture and an opaque disc of 2 mm diameter)
#select whether you are using "low", "high" or "none" to filter the image
filter="custom"

#with N_mask, we decide how many pixels we use. The pixel size depends on the dimensions of the system
N_mask, N_output = 1024, 1024
pixsize_mask = system_size / N_mask

#Real grid
x = np.linspace(-system_size / 2, system_size / 2, num=N_mask)
y = np.linspace(-system_size / 2, system_size / 2, num=N_mask)
xx, yy = np.meshgrid(x, y)

# x and y frequencies: these are the frequency ranges that show up in the fourier plane at distance f from the first lens
# with the object at z=0, lens 1 at z=f, fourier plane at z=2f

freq_x = fftpack.fftshift(fftpack.fftfreq(N_mask, d=pixsize_mask))
freq_y = fftpack.fftshift(fftpack.fftfreq(N_mask, d=pixsize_mask))

# these frequencies can be mapped to real coordinates in the plane of the lens focus:
x_freq=freq_x*wavelength*f
y_freq=freq_y*wavelength*f
xx_freq, yy_freq = np.meshgrid(x_freq, y_freq)

#Input: monochromatic laser field with given circular apperture, just like in the class demo
input_field = np.zeros((N_mask, N_mask))
input_field[np.sqrt(xx**2+yy**2) < laser_size/2] = 1

#Show input field in meters, with axis names
plt.imshow(input_field, extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
#plt.xlabel('x (m)')
#plt.ylabel('y (m)')
#plt.title("Laser Intensity")
plt.show()

#Import the Object from a jpg image
# you have to choose your own object!

mypath='Otica_aplicada/pattern2.png'


# _object is the object we are using in the first plane where z=0. We have to
# rescale the object with our coordinate system. The laser illuminates the object

from PIL import Image
# Load the PNG file using Pillow
img = Image.open(mypath)
# Convert the image to grayscale
img = img.convert('L')
# Resize the image to the desired number of pixels
img = img.resize((len(x), len(y)))
# Convert the image to a NumPy array
img_array = np.asarray(img)
# Normalize the array
object_ = img_array / 255.0

#Filter defintion
filter_low = np.zeros((N_mask, N_mask))
filter_low[np.sqrt(xx_freq**2+yy_freq**2) < filter_size_low/2] = 1

filter_high = np.ones((N_mask, N_mask))
filter_high[np.sqrt(xx_freq**2+yy_freq**2) < (filter_size_high/2)] = 0


input_field=input_field*object_

#Show input field in meters, with axis names
plt.imshow(input_field, extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
plt.savefig('input_field.jpg', dpi=300)
plt.show()


#From first lens to Fourier plane
fourier_plane = fftpack.fftshift(fftpack.fft2(fftpack.ifftshift(input_field)))


# Apply the custom function to create the filter
filter_custom = np.where((np.abs(fourier_plane)/1000) < 508.118078,
                         (1.06833 - 8.30262E-3 * (np.abs(fourier_plane)/1000) + 2.01025E-5 * (np.abs(fourier_plane)/1000)**2
                          + 4.90165E-8 * (np.abs(fourier_plane)/1000)**3 - 2.69883E-10 * (np.abs(fourier_plane)/1000)**4
                          + 2.82109E-13 * (np.abs(fourier_plane)/1000)**5), 0)
filter_custom = np.clip(filter_custom, 0, 1)

#Filter in the Fourier plane
if filter=="low":
    output_ft = fourier_plane*filter_low
elif filter=="high":
    output_ft = fourier_plane*filter_high
elif filter=="custom":
    output_ft = fourier_plane*filter_custom
elif filter=="none":
    output_ft = fourier_plane
else:
    print("Error: filter not defined, you can choose none")

#Intensity at the fourier plane of the second lens, with shift
output_field = np.abs(fftpack.ifftshift(fftpack.ifft2(fftpack.fftshift(output_ft))))

#Show results with independent colorbar and real scale

fig, axs = plt.subplots(2,2, figsize=(12,8))
fig.suptitle('Fourier optics')
axs[0,0].set_title('Input Field')
im_1=axs[0,0].imshow(input_field, extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
axs[0,0].set_xlabel('x (m)')
axs[0,0].set_ylabel('y (m)')

axs[0,1].set_title('Fourier Transform')
axs[0,1].set_xlabel('x (m)')
axs[0,1].set_ylabel('y (m)')
im_2=axs[0,1].imshow(np.abs(fourier_plane), extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
if filter=="low":
    axs[1,0].set_title('Fourier Transform with filter')
    im_3=axs[1,0].imshow(np.abs(fourier_plane)*filter_low, extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
    axs[1,0].set_xlabel('x (m)')
    axs[1,0].set_ylabel('y (m)')
elif filter=="high":
    axs[1,0].set_title('Fourier Transform with filter')
    im_3=axs[1,0].imshow(np.abs(fourier_plane)*filter_high, extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
    axs[1,0].set_xlabel('x (m)')
    axs[1,0].set_ylabel('y (m)')
elif filter=="none":
    axs[1,0].set_title('Fourier Transform without filter')
    im_3=axs[1,0].imshow(np.abs(fourier_plane), extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
    axs[1,0].set_xlabel('x (m)')
    axs[1,0].set_ylabel('y (m)')
elif filter=="custom":
    axs[1,0].set_title('Fourier Transform with custom filter')
    im_3=axs[1,0].imshow(np.abs(fourier_plane)*filter_custom, extent=[x_freq.min(), x_freq.max(), y_freq.min(), y_freq.max()])
    axs[1,0].set_xlabel('x (m)')
    axs[1,0].set_ylabel('y (m)')
else:
    print("Error: filter not defined, you can choose none")
    
axs[1,1].set_title('Output Field')
im_4=axs[1,1].imshow(output_field, extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
axs[1,1].set_xlabel('x (m)')
axs[1,1].set_ylabel('y (m)')
im_2.set_clim(0, 700)
im_3.set_clim(0, 700)

plt.subplots_adjust(left=0.085, bottom=0.068, right=0.93, top=0.88, wspace=0.486, hspace=0.245)

plt.savefig('galaxy_filtered.jpg', dpi=300)
plt.show()


plt.imshow(output_field, extent=[-system_size / 2, system_size / 2, -system_size / 2, system_size / 2])
plt.savefig('output_field.jpg', dpi=300)
plt.show()


"""
#print(input_field)#1102 1105
#print(output_field)#1099 1107

# Define the standard size
standard_size = (1100, 1100)

# Open the images
input_img = Image.open('input_field.jpg')
output_img = Image.open('output_field.jpg')

# Resize the images
input_img_resized = input_img.resize(standard_size)
output_img_resized = output_img.resize(standard_size)

# Convert the images to grayscale
input_img_resized = input_img_resized.convert('L')
output_img_resized = output_img_resized.convert('L')

# Convert the images to NumPy arrays
input_array = np.array(input_img_resized)
output_array = np.array(output_img_resized)

# Perform the difference operation
difference = np.subtract(output_array, input_array)

# Display the result
plt.imshow(difference)
plt.show()
"""