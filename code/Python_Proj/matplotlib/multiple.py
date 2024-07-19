import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi,2*np.pi,200)
Y1, Y2, Y3 = np.sin(x), np.cos(x), np.tan(x)
fig,ax = plt.subplots()
ax.plot(x,Y1, "C2", label = "sine") # plotar no mesmo gráfico duas coisas 
ax.plot(x,Y2, "C5", label = "cosine")
ax.plot(x,Y3, "C1", label = "tan")
# Coisas bonitas

fig.suptitle("Ondas Sinusoidais")
ax.set_title("Two waves, 90º apart")

ax.set_ylabel("f(x)") 
ax.set_xlabel("x")

#ax.set_xscale("log")
plt.legend(loc="upper right") # implica dar labels antes
plt.xticks(np.linspace(-2*np.pi,2*np.pi,8)) # escolher manualmente ticks 
plt.ylim(-5,5) #limites da escala
plt.grid()
#plt.savefig("test_image.png") # não funciona
plt.show()