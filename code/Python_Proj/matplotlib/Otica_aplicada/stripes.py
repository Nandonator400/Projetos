import numpy as np
import matplotlib.pyplot as plt

def generate_increasing_frequency_stripes(width, height, n = 43):
    m = n
    cnt = 0
    black = True
    image = np.zeros((height, width))   
    for x in range(width):
        if cnt < m and black == True:
            image[0:width-1,x] = 1
            cnt += 1
        elif cnt < m and black == False:
            image[0:width-1,x] = 0
            cnt += 1
        elif cnt == m and black == True:
            image[0:width-1,x] = 1
            cnt = 0
            m -= 1
            black = False
        elif cnt == m and black == False:
            image[0:width-1,x] = 0
            cnt = 0
            m -= 1
            black = True

    return image

# Define image dimensions
width = 1000
height = 800

# Generate the vertical stripe image with increasing frequency
increasing_frequency_stripe_image = generate_increasing_frequency_stripes(width, height)

# Display the image
plt.figure(figsize=(10, 8))
plt.imshow(increasing_frequency_stripe_image, cmap='gray', aspect='auto')
plt.axis('off')
plt.show()