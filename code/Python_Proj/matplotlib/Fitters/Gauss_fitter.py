import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from math import sqrt

################################################ read the file
file_path = "Fitters/data.ASC"

points = []
cnt = 0
with open(file_path, "r") as file:
    for line in file:
        if line.strip() == "": # skips junk lines in ,ASC
            cnt += 1
            continue
        if cnt == 1:
            elements = line.strip().split(",") # splits string lines by ","
            points.append(elements)

points.pop(0) # removes first garbage element
points = [[int(element) for element in inner_list] for inner_list in points] # converts str into int

###################################################################### Parameters

ROI = True
lower = 0
upper = 1023

bins = 100
transparency= 0.6
colour = "b"

################################################################### Create data set

def selector(Roi=False, vals=list[list[int]]): # uses o ROI
    if Roi == False:
        data = [element[0] for element in vals for _ in range(element[1])] # convert to histogram list
    else: # ROI ON
        data = [element[0] for element in vals for _ in range(element[1]) if element[2] == 1]
    return data

def selector_zone(vals=list[list[int]], lower=0, upper=1023): # uses boundaries
    data = [element[0] for element in vals for _ in range(element[1]) if (element[0] >= lower and element[0] <= upper)]
    return data

data = selector(ROI,points)
print("Number of points:",len(data))
#data = selector_zone(points,350,1023)

###################################################################### Create and fit histogram

mu, std = norm.fit(data) # get mean and std
 
plt.hist(data, bins=bins, density=True, alpha=transparency, color=colour) #  plot hist
xmin, xmax = plt.xlim() #plot pdf
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
 
plt.plot(x, p, linewidth=2, linestyle="--", color="red",label='Gausiana')
limite = plt.ylim()
print(limite)

######################## auxiliary lines 
ax = plt.gca()
y_gaus = 1/float(std*sqrt(2*np.pi)) # max value of gausian
y_max = ax.get_ylim()[1]
print()
FWHM_min = (mu - 1.175*std-ax.get_xlim()[0])/(ax.get_xlim()[1]-ax.get_xlim()[0])
FWHM_max=(mu + 1.175*std-ax.get_xlim()[0])/(ax.get_xlim()[1]-ax.get_xlim()[0])

plt.axvline(mu, color='purple', linestyle='--', linewidth=2, label='Mean',ymax=y_gaus/y_max)
plt.axhline(y_gaus/2.0, color='orange', linestyle='--', linewidth=2, label='FWHM',xmin= FWHM_min, xmax=FWHM_max)

########################
title = "μ: {:.2f}  Std: {:.2f}  FWHM: {:.2f}".format(mu, std, std*2.35)
plt.title(title)

plt.xlabel('Intensidade (Chn)')
plt.ylabel('Frequência relativa')
plt.legend(loc='upper right')
plt.grid(True)


plt.show()
