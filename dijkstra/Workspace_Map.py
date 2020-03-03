#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
#from google.colab.patches import cv2_imshow

class WorkspaceMap:
    def __init__(self,radius,clearance):
        
        self.radius = radius
        self.clearance = clearance
        self.height = 200
        self.width = 300
        #self.Surface = pg.display.set_mode((self.width,self.height))
        
        self.shift = self.radius+self.clearance
    
    def getMap(self):
        BLUE_COLOR = (255,0,0)
        BLACK_COLOR = (0,0,0)
        img = np.zeros((self.height,self.width,3),dtype=np.uint8)

        # coord_Poly = np.array([(self.height-(120-self.shift),20-self.shift),
        #               (self.height-(185+self.shift),25-self.shift),
        #               (self.height-(185+self.shift),75+self.shift),
        #               (self.height-(150+self.shift),100+self.shift),
        #               (self.height-(120-self.shift),75+self.shift),
        #               (self.height-(150-self.shift),50+self.shift)],dtype=np.int32).reshape((-1,1,2))

        coord_Poly = np.array([(25-self.shift,self.height-(185+self.shift)),
                               (75+self.shift,self.height-(185+self.shift)),
                               (100+self.shift,self.height-(150+self.shift)),
                               (75+self.shift,self.height-(120-self.shift)),
                               (50+self.shift,self.height-(150-self.shift)),
                               (20-self.shift,self.height-(120-self.shift))],dtype=np.int32)
        coord_rect = np.array([(30-self.shift,self.height-(67.5+self.shift)),
                      (35+self.shift,self.height-(76+self.shift)),
                      (100+self.shift,self.height-(38.6-self.shift)),
                      (95-self.shift,self.height-(30-self.shift))],dtype = np.int32).reshape((-1,1,2))
        
        coord_rhom = np.array([(225,self.height-(40+self.shift)),
                      (250+self.shift,self.height-25),
                      (225,self.height-(10-self.shift)),
                      (200-self.shift,self.height-25)],dtype=np.int32).reshape((-1,1,2))

        cv2.rectangle(img,(0,0),(self.width,self.height),BLUE_COLOR,5)
        cv2.fillPoly(img,[coord_Poly],BLUE_COLOR)
        cv2.fillConvexPoly(img,coord_rect,BLUE_COLOR)
        cv2.fillConvexPoly(img,coord_rhom,BLUE_COLOR)
        cv2.circle(img,(225,self.height-150),25+self.shift,BLUE_COLOR,-1)
        cv2.ellipse(img,(150,self.height-100),(80+self.shift,40+self.shift),0,0,360,BLUE_COLOR,-1)
     
        return img

    def start_visualization(self,img,initial_pos,visited_nodes,path):
	    try: 
		actions = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1], 
		           'UL': [-1, -1], 'UR': [-1, 1], 'DL': [1, -1], 'DR': [1, 1]}

		initial_pos = list(initial_pos)

		for node in visited_nodes:
		    img[node] = 1
		    cv2.imshow('Map', img)
		    #time.sleep(0.001)

		next_pos = initial_pos
		for action in path:
		    next_pos = np.add(next_pos, actions[action])
		    img[tuple(next_pos)] = 0
		    cv2.imshow('Map', img)
		    #time.sleep(0.01)

		cv2.imshow('Map', img)
	    except:
		print(-99999)
	    cv2.waitKey(0)
	    cv2.destroyAllWindows()



# In[ ]:

Map = WorkspaceMap(2,2)
print("Total shift",Map.shift)
map_layout = Map.getMap() 
#cv2.imshow('MAP',map_layout)
WHITE_COLOR = (255,255,255)


#for i in range(100):
#	map_layout[i,i+2]= WHITE_COLOR
#	cv2.imshow('img',map_layout)
	#time.sleep(0.5)



# In[ ]:




