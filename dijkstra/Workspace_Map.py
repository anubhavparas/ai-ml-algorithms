#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pygame as pg
import cv2

#pg.init()
class WorkspaceMap:
    def __init__(self,radius,clearance):
        
        self.radius = radius
        self.clearance = clearance
        self.height = 200
        self.width = 300
        #self.Surface = pg.display.set_mode((self.width,self.height))
        self.shift = self.radius+self.clearance
    
    def getMap(self,window):
        BLUE_COLOR = (0,0,255)
        BLACK_COLOR = (0,0,0)
        window.fill(BLACK_COLOR)
        coord_Poly = [(20-self.shift,self.height-(120-self.shift)),
                      (25-self.shift,self.height-(185+self.shift)),
                      (75+self.shift,self.height-(185+self.shift)),
                      (100+self.shift,self.height-(150+self.shift)),
                      (75+self.shift,self.height-(120-self.shift)),
                      (50+self.shift,self.height-(150-self.shift))]
        coord_rect = [(30-self.shift,self.height-(67.5+self.shift)),
                      (35+self.shift,self.height-(76+self.shift)),
                      (100+self.shift,self.height-(38.6-self.shift)),
                      (95-self.shift,self.height-(30-self.shift))]
        #circle = [(25+self.ax,225)]
        coord_rhom = [(225,self.height-(40+self.shift)),
                      (250+self.shift,self.height-25),
                      (225,self.height-(10-self.shift)),
                      (200-self.shift,self.height-25)]
        poly1 = pg.draw.polygon(window,BLUE_COLOR,coord_Poly,0)
        poly2 = pg.draw.polygon(window,BLUE_COLOR,coord_rect,0)
        poly3 = pg.draw.polygon(window,BLUE_COLOR,coord_rhom,0)
        circle = pg.draw.circle(window,BLUE_COLOR,(225,self.height-125),25+self.shift,0)
        ellipse = pg.draw.ellipse(window,BLUE_COLOR,(150,self.height-100,80+self.shift,40+self.shift),0)
        Map_ = [poly1,poly2,poly3,circle,ellipse]
        return Map_
        


# In[ ]:


m = WorkspaceMap(2,1)
pg.init()
window = pg.display.set_mode((300,200))
MAP = m.getMap(window)
while True:
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit
            quit()
    #print(MAP)
    pg.display.update()


# In[ ]:




