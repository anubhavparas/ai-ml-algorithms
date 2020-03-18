import math
import numpy as np
from input_receiver import receive_inputs
from pathexplorer import PathExplorer
from configurationspace import ConfigurationSpace
from heuristics import EUCL_HEURISTIC, MANHTN_HEURISTIC


if __name__ == "__main__":

    is_input_valid, init_pos, target_pos, orientation, robot_radius, clearance_req, step_size = receive_inputs(is_robot_rigid = False)

    if is_input_valid:
        init_pos = init_pos[1], init_pos[0]
        target_pos = target_pos[1], target_pos[0]

        c_space = ConfigurationSpace(height=200, width=300)
        c_space_map = c_space.get_cspace_map()

        path_explorer = PathExplorer()
        path_explorer.find_path(init_pos, target_pos, orientation, step_size, c_space_map, EUCL_HEURISTIC)

        

     

