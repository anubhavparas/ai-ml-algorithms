import numpy as np
import cv2
from cspacepredicatesupplier import CSpacePredicateSupplier
from obstacle_check import *
from functools import reduce

class ConfigurationSpace:
    def __init__(self, height, width, radius_of_bot=0, clearance=0):
        self.height = height
        self.width = width
        self.padding = radius_of_bot + clearance
        padding = self.padding




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

    def get_cspace_map(self):
        print('\nGetting configuration space...')
        padding = self.padding
        height = self.height
        width = self.width

        BLUE_COLOR = (255,0,0)
        img = np.zeros((height, width, 3), dtype=np.uint8)

        obstacle_predicates = CSpacePredicateSupplier().get_cspace_predicates(height, width, padding)
        predicate_or_op = lambda predicate1, predicate2: predicate1 or predicate2 

        for y in range(0, height):
            for x in range(0, width):
                is_point_in_obstacle = reduce(predicate_or_op, [obstacle_predicate(x,y) for obstacle_predicate in obstacle_predicates])
                if is_point_in_obstacle:
                    img[y, x] = BLUE_COLOR

        print('Configuration space initialized.\n')
        return img


    def check_for_obstacles(self, p1, p2):
        predicate_or_op = lambda predicate1, predicate2: predicate1 or predicate2
        is_action_invalid = reduce(predicate_or_op, [
            check_for_boundary_padding(p2[1], p2[0], self.width, self.height, self.padding),
            checkCircleIntersection(p1, p2, self.circle[0], self.circle[1]),
            checkEllipseIntersection(p1, p2, self.ellipse[0], self.ellipse[1]),
            checkPolyIntersection(p1, p2, self.coord_poly),
            checkPolyIntersection(p1, p2, self.coord_rect),
            checkPolyIntersection(p1, p2, self.coord_rhom)
            ])
        return is_action_invalid


