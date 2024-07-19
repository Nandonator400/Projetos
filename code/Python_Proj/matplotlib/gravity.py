
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from time import time
import random
from math import sqrt
random.seed(time())

""" 
TO DO

1 object creator -> speed vector, position vector, applied force 
2 Grid creator -> with extra rows to scout the edges
3 Grid reader -> (usa a func anterior) Big reader and a local reader 
4 Interactor function -> escaping sides and collisions with probability 
5 optimizer function -> determinar computação mínima aceitável 
6 displayer of animation
7 Animation pretiness
8 threading?
9 Separar em import files 

"""

### 1 ###

class Point:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.vel = [0,0]

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.mass}, {self.vel})"
    
    def get_x(self):
        return int(self.x)

    def get_y(self):
        return int(self.y)
    
    def get_mass(self):
        return float(self.mass)
    
    def get_speed(self):
        return self.vel

    def position(self, x_c, y_c):
        self.x = x_c
        self.y = y_c

    def velocity(self, speed_vect):
        self.vel = speed_vect

### 2 ###

def grid_creator(size, prob, max_mass):
    if size < 10 or prob <= 0 or prob >= 1 or max_mass <= 0:
        raise ValueError("Invalid input")
    
    grid = np.empty((size, size), dtype=object)
    for i in range(size):
        for j in range(size):
            z = 0
            if random.randint(0,100)/100.0 <= prob:
                point_mass = random.randint(0,100)/100.0* max_mass
                grid[i, j] = Point(i, j, round(point_mass,2)) 
    return grid
           
def grid_viewer():
    grid = grid_creator(100,0.5,20)
    for row in grid:
        print(row)

### 3 ###

def edge_definer(grid:list[Point], tolerance=int): #dada uma grid devolve a lista de pontos do edge com tolerênacia 
    # todas as listas começam em [0,0] e têm de ser quadradas 
    if tolerance <= 0:
        raise ValueError("Invalid Paramethers")
    size = len(grid[0])
    edge_points = []
    for i in grid:
        for j in i: 
            if grid[i,j].get_x():
                edge_points.append(grid[i,j]) # WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG
    
    print(1) # para ler os cantos ?

def local_vector():
    print(1) # para as caixas locais 

def big_vector():
    print(1) # para a caixa grande 

def force_vector(obj1=Point, obj2=Point):
    G = 6.6743E-11
    distance_sqrd = (obj1.get_x() -obj2.get_x())**2 + (obj1.get_y() -obj2.get_y())**2
    magnitude = G * obj1.get_mass() * obj2.get_mass() / float(distance_sqrd)
    # vector from obj 1 to obj2
    direction = ((obj2.get_x() -obj1.get_x())/sqrt(distance_sqrd), (obj2.get_y() -obj1.get_y())/sqrt(distance_sqrd)) 
    return (direction[0], direction[1], magnitude)

def vector_weighter():
    print(1) # juntar os vetores todos e fazer uma média ponderada 

### Testing zone ###
grid_viewer()
print(force_vector(Point(1, 1, 3E10),Point(2,2,2)))