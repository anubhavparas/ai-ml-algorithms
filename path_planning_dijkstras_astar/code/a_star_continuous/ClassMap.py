#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import time
#from google.colab.patches import cv2_imshow

class WorkspaceMap:
    def __init__(self,radius,clearance):
        
        self.radius = radius
        self.clearance = clearance
        self.height = 200
        self.width = 300
        
        self.padding = self.radius+self.clearance
        padding = self.padding
        height = self.height
        width = self.width

        self.coord_poly = np.array([(25-padding, 185+padding),
                               (75+padding, 185+padding),
                               (100+padding, 150+padding),
                               (75+padding, 120-padding),
                               (50+padding, 150-padding),
                               (20-padding, 120-padding)], dtype='int')
        
        self.coord_rect = np.array([(30-padding, 67.5+padding),
                      (35+padding, 76+padding),
                      (100+padding, 38.6-padding),
                      (95-padding, 30-padding)], dtype = 'int')
        
        self.coord_rhom = np.array([(225, 40+padding),
                      (250+ padding, 25),
                      (225, 10-padding),
                      (200-padding, 25)], dtype='int')
        self.circle = [(25+padding),(225,150)]
        self.ellipse = [(80+padding,40+padding),(150,100)]

    def plotMap(self):
        height = self.height
        width = self.width
        padding =  self.padding
        poly_pts = self.coord_poly
        rect_pts = self.coord_rect
        rhom_pts = self.coord_rhom
        circle = self.circle
        ellipse = self.ellipse
        
        fig = plt.figure()
        fig.set_dpi(100)
        fig.set_size_inches(8.5,6)
        ax = plt.axes(xlim=(0,width),ylim=(0,height))
        cir = plt.Circle((circle[1]),circle[0],fc=None)
        rect = plt.Polygon(rect_pts)
        rhom = plt.Polygon(rhom_pts)
        poly = plt.Polygon(poly_pts)
        ell= Ellipse((ellipse[1]),ellipse[0][0],ellipse[0][1],0)
        shapes = [cir,rect,rhom,poly,ell]
        for shape in shapes:
            plt.gca().add_patch(shape)
        return fig


# In[38]:


Map = WorkspaceMap(5,5)
fig = Map.plotMap()


#plt.show()


# In[ ]:





# In[ ]:




