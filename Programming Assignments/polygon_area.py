import math

def polysum(n,s):
    ''' This function takes in n representing the number of sides for the polygon and s representing
the lenght of each side. It will then return the sum of area for the polygon and the square of the 
perimeter of the polygon.
    '''
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    perimeter = n*s
    perimetersq = perimeter**2
    sumap= area+perimetersq
    
    return round(sumap, 4)
