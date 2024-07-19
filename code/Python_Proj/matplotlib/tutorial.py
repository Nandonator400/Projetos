import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2 * np.pi, 200) # cria um vetor de pontos no eixo dos x
y = np.sinh(x) # aplica o vetor a uma função e retorna um vetor 

fig, ax = plt.subplots() # prepara os plots 

ax.plot(x,y, linestyle = "--") # dá plot dos dados (só um por vez)
plt.show() # mostra os plots 


