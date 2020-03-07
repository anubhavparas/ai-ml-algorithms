import numpy as np
import cv2
from cspacepredicatesupplier import CSpacePredicateSupplier
from functools import reduce

class ConfigurationSpace:
    def __init__(self, height, width, radius_of_bot=0, clearance=0):
        self.height = height
        self.width = width
        self.padding = radius_of_bot + clearance

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
