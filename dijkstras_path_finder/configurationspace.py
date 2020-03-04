import numpy as np
import cv2

class ConfigurationSpace:
    def __init__(self, height, width, radius_of_bot=0, clearance=0):
        self.height = height
        self.width = width
        self.padding = radius_of_bot + clearance

    def get_cspace_map(self):
        padding = self.padding
        height = self.height
        width = self.width

        BLUE_COLOR = (255,0,0)
        img = np.zeros((height, width, 3), dtype=np.uint8)

        coord_poly = np.array([(25-padding, height-(185+padding)),
                               (75+padding, height-(185+padding)),
                               (100+padding, height-(150+padding)),
                               (75+padding, height-(120-padding)),
                               (50+padding, height-(150-padding)),
                               (20-padding, height-(120-padding))], dtype=np.int32)
        
        coord_rect = np.array([(30-padding, height-(67.5+padding)),
                      (35+padding, height-(76+padding)),
                      (100+padding, height-(38.6-padding)),
                      (95-padding, height-(30-padding))], dtype = np.int32).reshape((-1,1,2))
        
        coord_rhom = np.array([(225, height-(40+padding)),
                      (250+ padding, height-25),
                      (225, height-(10-padding)),
                      (200-padding, height-25)], dtype=np.int32).reshape((-1,1,2))

        if  padding:
            cv2.rectangle(img, (0,0), (width-1, height-1), BLUE_COLOR, padding)
        
        cv2.fillPoly(img, [coord_poly], BLUE_COLOR)
        cv2.fillConvexPoly(img, coord_rect, BLUE_COLOR)
        cv2.fillConvexPoly(img, coord_rhom, BLUE_COLOR)
        cv2.circle(img, (225, height-150), (25+padding), BLUE_COLOR, -1)
        cv2.ellipse(img, (150, height-100), (40+padding, 20+padding), 0, 0, 360, BLUE_COLOR, -1)
     
        return img

    
