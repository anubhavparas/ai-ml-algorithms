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
    m,y_int,x_int = lineModelGenerator(p1,p2)
    q = center[1]
    p = center[0]
    
    if m == np.inf:
        A = 1
        B = -2*q
        C = q**2 + x_int**2 + p**2 - r**2 - 2*x_int*p
        flag  = 1
    else:
        A = 1+m**2
        B = 2*(m*y_int - m*q - p)
        C = q**2 - r**2 + p**2 -2*y_int*q + y_int**2
        flag = 0
        
    disc = B**2 - 4*A*C
   
    if disc < 0:
        return False
    else:
        if flag == 0:
            x1 = (-B+math.sqrt(disc))/(2*A)
            x2 = (-B-math.sqrt(disc))/(2*A)
        elif flag == 1:
            x1 = x_int
            x2 = x1

    if min(p1[0],p2[0])<=x1<=max(p1[0],p2[0]) or min(p1[0],p2[0])<=x2<=max(p1[0],p2[0]):
        return True
    else:
        return False
        
# Ellipse: 
# @Params: Segment pt1, pt2, ellipse params,center
# Return type: bool
def checkEllipseIntersection(p1,p2,ell_param,center):
    m,y_int,x_int = lineModelGenerator(p1,p2)
    
    h = center[0]
    k = center[1]
    a = ell_param[0]
    b = ell_param[1]
    if m == np.inf:
        A = 1
        B = -2*k
        C = k**2 - b**2 + ((x_int-h)**2)*((b**2)/(a**2))
        flag = 1
    else:    
        A = (a**2)*(m**2) + b**2
        B = 2*(-((h**2)*(b**2))+(a**2)*m*(y_int-k))
        C = (h**2)*(b**2) + (a**2)*((y_int-k)**2) - (a**2)*(b**2)
        flag = 0
    
    #Checking if the quadratic equation has unique real roots
    disc = B**2 - 4*A*C
    if disc < 0:
        return False
    else:
        if flag == 0:
            x1 = (-B+math.sqrt(disc))/(2*A)
            x2 = (-B-math.sqrt(disc))/(2*A)
        elif flag == 1:
            x1 = x_int
            x2 = x1

    if min(p1[0],p2[0])<=x1<=max(p1[0],p2[0]) or min(p1[0],p2[0])<=x2<=max(p1[0],p2[0]):
        return True
    else:
        return False

# Polygon: 
# @Params: Segment pt1, pt2, coordinates of polygon
# Return type: bool
def checkPolyIntersection(p1,p2,coord):
    x_poly_coord = coord[:,0]
    y_poly_coord = coord[:,1]
    flag = 0
    polyLines_model = [] 
    M,Y_int,X_int = lineModelGenerator(p1,p2)
    
    for i in range(len(coord)):
        if i+1 >= len(coord):
            polyLines_model.append(lineModelGenerator(coord[i],coord[0]))
        else:    
            polyLines_model.append(lineModelGenerator(coord[i],coord[i+1]))
    
    print(polyLines_model)
    for ix,model in enumerate(polyLines_model):
        m_poly = model[0]
        y_int_poly = model[1]
        x_int_poly = model[2]
        
        if m_poly == np.inf:
            x = x_int_poly
#             m_poly = M
#             y_int_poly = Y_int
        else:
            #if M!=np.inf:
            num = y_int_poly - Y_int
            den = M - m_poly
            x =  num/den
#             else:
#                 x = X_int 
                
        #y = m_poly*x + y_int_poly
        y = M*x + Y_int
        if min(p1[0],p2[0])<x<=max(p1[0],p2[0]) and min(p1[1],p2[1])<y<=max(p1[1],p2[1]):
            if ix+1 >= len(coord):
                if min(x_poly_coord[ix],x_poly_coord[0])<=x<=max(x_poly_coord[ix],x_poly_coord[0]) and min(y_poly_coord[ix],y_poly_coord[0])<=y<=max(y_poly_coord[ix],y_poly_coord[0]):
                    flag+=1
                
            else:
                if min(x_poly_coord[ix],x_poly_coord[ix+1])<=x<=max(x_poly_coord[ix],x_poly_coord[ix+1]) and min(y_poly_coord[ix],y_poly_coord[ix+1])<=y<=max(y_poly_coord[ix],y_poly_coord[ix+1]):
                    flag+=1
                
    if flag > 0:
        return True
    else:
        return False        
    
def lineModelGenerator(l1,l2):
    if l1[0] == l2[0]:
        x_intercept = l2[0]
        m = np.inf
        y_intercept = np.inf
    else:
        m = (l2[1]-l1[1])/(l2[0]-l1[0])
        y_intercept = l2[1]-m*l2[0]
        x_intercept = 0
    return m,y_intercept,x_intercept

# def boundaryCondition(coord,x,y):
#     X_poly = coord[:,0]
#     Y_poly = coord[:,1]
#     flag = 0
#     for i in range(len(coord)):
#         if i+1 >= len(coord):
#             if min(X_poly[i],X_poly[0])<=x<=max(X_poly[i],X_poly[0]) and min(Y_poly[i],Y_poly[0])<=y<=max(Y_poly[i],Y_poly[0]):
#                 flag+=1
# #             if x in range(min(X_poly[i],X_poly[0]),max(X_poly[i],X_poly[0])) and y in range(min(Y_poly[i],Y_poly[0]),max(Y_poly[i],Y_poly[0])):
# #                 flag+=1
#         else:
#             if min(X_poly[i],X_poly[i+1])<=x<=max(X_poly[i],X_poly[i+1]) and min(Y_poly[i],Y_poly[i+1])<=y<=max(Y_poly[i],Y_poly[i+1]):
#                 flag+=1
#     if flag > 0:
#         return True
#     return False
