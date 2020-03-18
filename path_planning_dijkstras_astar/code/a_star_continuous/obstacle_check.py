#!/usr/bin/env python
# coding: utf-8

# In[95]:


import math
import numpy as np
import matplotlib.pyplot as plt

'''
Checking if the line intersects closed figure
1. Circle
2. Ellipse
3. Polygon
'''

# Circle: 
# @Params: Segment pt1, pt2,radius,center
# Return type: bool
def checkCircleIntersection(p1,p2,r,center):
    m,c = lineModelGenerator(p1,p2)
    q = center[1]
    p = center[0]
    
    A = 1+m**2
    B = 2*(m*c - m*q - p)
    C = q**2 - r**2 + p**2 -2*c*q + c**2
    
    disc = B**2 - 4*A*C
   
    if disc < 0:
        return False
    else:
        x1 = (-B+math.sqrt(disc))/(2*A)
        x2 = (-B-math.sqrt(disc))/(2*A)

        if p1[0]<=x1<=p2[0] or p1[0]<=x2<=p2[0]:
            return True
        else:
            return False
        
# Ellipse: 
# @Params: Segment pt1, pt2, ellipse params,center
# Return type: bool
def checkEllipseIntersection(p1,p2,ell_param,center):
    m,c = lineModelGenerator(p1,p2)
    
    a = ell_param[0]
    b = ell_param[1]

    A = (a**2)*(m**2) + b**2
    B = 2*(a**2)*m*c
    C = (a**2)*((c**2)-(b**2))
    
    #Checking if the quadratic equation has unique real roots
    disc = B**2 - 4*A*C
    if disc < 0:
        return False
    else:
        x1 = (-B+math.sqrt(disc))/(2*A)
        x2 = (-B-math.sqrt(disc))/(2*A)

        if p1[0]<=x1<=p2[0] or p1[0]<=x2<=p2[0]:
            return True
        else:
            return False

# Polygon: 
# @Params: Segment pt1, pt2, coordinates of polygon
# Return type: bool
def checkPolyIntersection(p1,p2,coord):
    x = coord[:,0]
    y = coord[:,1]
    
    polyLines_model = [] 
    M,C = lineModelGenerator(p1,p2)
    for i in range(len(coord)):
        if i+1 >= len(coord):
            polyLines_model.append(lineModelGenerator(coord[i],coord[0]))
        else:    
            polyLines_model.append(lineModelGenerator(coord[i],coord[i+1]))
        
    print(polyLines_model)
    for model in polyLines_model:
        num = model[1] - C
        if model[0] == np.inf:
            x = model[1]
        else:
            den = M - model[0]
            x =  num/den
        y = M*x+C
        if p1[0]<x<=p2[0] and p1[1]<y<p2[1]:
            return True
        else:
            return False

def lineModelGenerator(l1,l2):
    if l1[0] == l2[0]:
        c = l2[0]
        m = np.inf
    else:
        m = (l2[1]-l1[1])/(l2[0]-l1[0])
        c = l2[1]-m*l2[0]
    return m,c


# In[94]:


coord = np.array([(1,5),(5,5),(5,1),(1,1)],dtype = np.int32)
print(coord[0])
#result = checkPolyIntersection(line,coord)
circ_r = 2
circ_cent = (0,5)
l1 = (0,5)
l2 = (3,11)
#r = checkCircleIntersection(l1,l2,circ_r,circ_cent)
result = checkPolyIntersection(l1,l2,coord)
#print(lineModelGenerator(l1,l2))
#print(r)
print(result)


# In[ ]:





# In[ ]:




