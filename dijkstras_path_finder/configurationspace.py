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

        c_space_predicates = CSpacePredicateSupplier().get_cspace_predicates(height, width, padding)
        for y in range(0, height):
            for x in range(0, width):
                is_point_in_obstacle = reduce(self.predicate_or_op, [c_space_predicate(x,y) for c_space_predicate in c_space_predicates])
                if is_point_in_obstacle:
                    img[y, x] = BLUE_COLOR

        print('Configuration space initialized.\n')
        return img


    def predicate_or_op(self, predicate1, predicate2):
        return predicate1 or predicate2


    