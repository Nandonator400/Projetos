import matplotlib.pyplot as plt
import numpy as np

n = int(1E4)
x = np.random.normal(0,2,n)
fig,ax = plt.subplots()
ax.hist(x, color = "cyan", bins = int(n/100)) # cor
plt.show()

