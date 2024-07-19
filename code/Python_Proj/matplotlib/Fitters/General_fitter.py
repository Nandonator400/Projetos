import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import inspect

############################################### COMMAND CENTRAL

file_path = "Fitters/data.ASC"
ROI = False
lower = 0
upper = 1023
bins = 100
transparency= 0.6
colour = "b"
decimals = 3
# for changing selection method: line 68

############################################### Define func here!

def func2(x, mu, sigma, c): #Gausian
    return 1/(sigma * np.sqrt(2*np.pi))*np.exp(-0.5*(x-mu)**2/(sigma**2)+c)

def func1(x, a, b, c, d): #Exponential
    x = np.asarray(x)
    return a*(2.718281828459045)**(b*(x-d))+ c

def func(x,a,b): # linear
    x = np.asarray(x)
    return a + b*x

initial_guesses = [1400,2.5] # PLEASE GIVE SOME GUESSES FOR THE FIT!

################################################ read the file

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

################################################################### Create data set

def selector(Roi=False, vals=list[list[int]]): # uses o ROI
    if Roi == False:
        x = np.linspace(vals[0][0],vals[-1][0],len(vals)) # considera que começa em 0
        y = [element[1] for element in vals] # convert to histogram list

    else: # ROI ON
        data = [element[0] for element in vals if element[2] == 1]
        x = np.linspace(vals[min(data)][0],vals[max(data)][0],vals[max(data)][0]-vals[min(data)][0]+1)
        y = [element[1] for element in vals if element[2] == 1] # convert to histogram list
    return (x,y)

def selector_zone(vals=list[list[int]], lower=0, upper=1023): # uses boundaries
    x = [element[0] for element in vals if (element[0] >= lower and element[0] <= upper)]
    y = [element[1] for element in vals if (element[0] >= lower and element[0] <= upper)]
    return (x,y)

#data = selector(ROI, points)
data = selector_zone(points,350,1023)
#x = [750,775,800,825,850,875,900,925,950,975,1000,1025,1050,1075,1100,1125,1150,1175,1200]
#y = [395,447,515,519,579,572,573,570,598,565,619,579,660,620,649,646,652,644, 663]
#data = [x,y]

####################################################################
parameters_dict = inspect.signature(func).parameters
parameter_labels = list(parameters_dict.keys())[1:] #retrieves names of args

num_args = len(inspect.signature(func).parameters)-1 #get the number of args in func

optimized_cts, covariance = curve_fit(func, data[0], data[1],p0=initial_guesses)

residuals = data[1] - func(data[0], *optimized_cts)
rms = np.sqrt(np.mean(residuals**2))

print("Covariâncias:")
print(covariance)
print("Optimized values:")
print(optimized_cts)
print("RMS value:", rms)
###################################################################

plt.scatter(data[0],data[1],s=1, label="Exp data")
plt.plot(data[0], [func(element, *optimized_cts) for element in data[0]], #unpacks args
         color="red", linestyle="--", label="fit")

plt.xlabel('Intensidade (Chn)')
plt.ylabel('Frequência')
plt.legend(loc='upper right')
plt.grid(True)
plt.title("Gráfico fitado")

plt.text(0.05,0.9,f'Rms = {rms:.{decimals}f}',transform=plt.gca().transAxes)
for i, parameter in enumerate(optimized_cts):
    plt.text(0.05, 0.85 - i * 0.05, f'{parameter_labels[i]} = {parameter:.{decimals}f}', transform=plt.gca().transAxes)
plt.show()
