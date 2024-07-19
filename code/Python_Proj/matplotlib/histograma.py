import matplotlib.pyplot as plt
import numpy as np

n = 1500
x = np.random.binomial(40,0.5,n)
fig, ax = plt.subplots() # prepara os plots 
ax.hist(x, color = "cyan", bins = 20) # cor
plt.show()
