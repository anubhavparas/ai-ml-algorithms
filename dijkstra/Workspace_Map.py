#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pygame as pg
import cv2

#pg.init()
class drawMap:
    def __init__(self,radius,clearance):
        
        self.R = radius
        self.C = clearance
        self.height = 200
        self.width = 300
        #self.Surface = pg.display.set_mode((self.width,self.height))
        self.ax = self.R+self.C
    
    def getMap(self,window):
        blue = (0,0,255)
        white = (255,255,255)
        window.fill(white)
        coord_Poly = [(20-self.ax,self.height-(120-self.ax)),
                      (25-self.ax,self.height-(185+self.ax)),
                      (75+self.ax,self.height-(185+self.ax)),
                      (100+self.ax,self.height-(150+self.ax)),
                      (75+self.ax,self.height-(120-self.ax)),
                      (50,self.height-(150-self.ax))]
        coord_rect = [(30-self.ax,self.height-(67.5+self.ax)),
                      (35+self.ax,self.height-(76+self.ax)),
                      (100+self.ax,self.height-(38.6-self.ax)),
                      (95-self.ax,self.height-(30-self.ax))]
        #circle = [(25+self.ax,225)]
        coord_rhom = [(225,self.height-(40+self.ax)),
                      (250+self.ax,self.height-25),
                      (225,self.height-(10-self.ax)),
                      (200-self.ax,self.height-25)]
        poly1 = pg.draw.polygon(window,blue,coord_Poly,0)
        poly2 = pg.draw.polygon(window,blue,coord_rect,0)
        poly3 = pg.draw.polygon(window,blue,coord_rhom,0)
        circle = pg.draw.circle(window,blue,(225,self.height-125),25+self.ax,0)
        ellipse = pg.draw.ellipse(window,blue,(150,self.height-100,80+self.ax,40+self.ax),0)
        Map_ = [poly1,poly2,poly3,circle,ellipse]
        return Map_
        


# In[ ]:


m = drawMap(2,1)
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




