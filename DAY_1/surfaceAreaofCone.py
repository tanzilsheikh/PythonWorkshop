import math 

pi = math.pi 
# Function To Calculate Surface Area of Cone 

def surfacearea(r, s): 

    return pi * r * s + pi * r * r 

# Function To Calculate Total Surface Area 
# of Cylinder 

def totalsurfacearea(r, h): 

    tsurf_ar = (2 * pi * r * h) + (2 * pi * r * r) 

    return tsurf_ar 
  
# Driver Code 

radius = float(5) 

height = float(12) 

slat_height = float(13) 

r = 5

h = 8
print( "Surface Area Of Cone : ", surfacearea(radius, slat_height) )

print("Total  Surface Area  Of Cylinder =  ",totalsurfacearea(r,h))
