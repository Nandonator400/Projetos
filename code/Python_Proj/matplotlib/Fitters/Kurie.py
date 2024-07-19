from math import sqrt

# para funcionar deter ter um file "points.txt" onde a primeira linha é o bin 0 do MCA´
# tudo antes do 0 e para lá do 1023 deve ser apagado
filename = 'points.txt'
vals = []
f = open(filename, "r")
for line in f:
    values = line.strip().split(',')
    values.pop()
    values[0] = int(values[0])
    values[1] = int(values[1])
    vals.append(values)

min_val = 6
max_val = 140

#y = a + bx
a = -2.13E-03
b = 4.64E-03
x_vals = [0, 0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.2,1.4,1.6,1.8,2,2.2,2.4]
y_vals = [28.26,28.19,27.99,27.67,27.25,26.76,26.23,25.66,25.09,24.53,23.98,22.95,22.01,21.17,20.41,19.72,19.10,18.54]
data = []

for i in vals:
    if i[0] >= min_val and i[0]<=max_val:
        energy = a + float(b*i[0]) 
        w = energy / 0.511 + 1
        p = sqrt(w*w-1)
        index = 0
        for z in x_vals:
            if p > z:
                index += 1
            else:
                break
        g = y_vals[index] + (y_vals[index+1]-y_vals[index])/(x_vals[index+1]-x_vals[index])*(p-x_vals[index])
        t = 1/float(w) * sqrt(i[1]/float(g)) 
        temp_data = [i[0], energy, i[1],w,p,g,t]
        data.append(temp_data)

for element in data:
    print(element[1], element[6])
