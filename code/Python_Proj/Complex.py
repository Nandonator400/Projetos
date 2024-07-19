##################################### Complex calculator

import math

class complex:
    def sum(self, i:list, j:list): #sums up 
        result = list(map(lambda x, y: x + y, i, j))
        return result
    
    def multiply_canonic(self, i:list, j:list): # usual multiplication
        result = [i[0]*j[0]-i[1]*j[1]]
        result.append(i[0]*j[1]+i[1]*j[0])
        return result
    
    def multiply_polar(self, i:list, j:list): # polar multiplication
        result = [i[0]*j[0], i[1]+i[1]]
        return result
    
    def divide_polar(self, i:list, j:list): # polar division
        result = [i[0]/float(j[0]), i[1]-i[1]]
        return result
        

    def to_polar(self, i:list): # Converts canonic into polar 
        r = math.sqrt(i[0]**2 + i[1]**2)
        theta = math.atan2(i[1],i[0])
        return(list[r,theta])
        
    def to_canonic(self, i:list): # receives a list with the modulus r and the angle theta
        result = [i[0]*math.cos(i[1]),i[0]*math.sin(i[1])]
        return result
    
    def divide_canonic(self, i:list, j:list): # canonic division
        pol1, pol2 = self.to_polar(i), self.to_polar(j)
        aux = self.divide_polar(pol1,pol2)
        ans = self.to_canonic(aux)
        return aux
    
    def polar_power(self, i:list, power:int):
        result = [pow(i[0],power),i[1]*power]
        return result
    
    def canonic_power(self, i:list, power:int):
        pol = self.to_polar(i)
        pol = self.polar_power(pol)
        pol = self.to_canonic(pol)
        return pol
    
    def polar_roots(self, i:list, root:int): # retruns list with several polar solutions of a root if valid
        if root <= 0:
            raise ValueError("NON INTEGER VALUES NOT ALLOWED")
        r = i[0]**(1/float(root))
        angles=[(i[1]*2*math.pi*x)/float(root) for x in range(root)]
        roots = [[r,y] for y in angles]
        return roots
    
    def canonic_roots(self, i:list, root:int): # same as before but for canonic
        polar = self.to_polar(i)
        roots = self.polar_roots(polar, root)
        return roots
    
    def canonic_abs(self, i:list):
        return float(math.sqrt(i[0]**2 + i[1]**2))
    
    def argument(self, i:list):
        return math.atan2(i[1],i[0])
    
    def canonic_sin(self, i:list):
        aux1=self.to_canonic([math.exp(-i[1]), i[0]- math.pi/2])
        aux2=self.to_canonic([-math.exp(i[0],-i[0]- math.pi/2)])
        result = self.sum(aux1,aux2)
        return result

    # falta definir cos, sinh, cosh,

##################################### Complex calculator