import math
import numpy as np
from pathexplorer import PathExplorer
from configurationspace import ConfigurationSpace


if __name__ == "__main__":
    print(">> Bottom left corner is considered as (0,0)")
    print(">> Enter the initial and target positions, radius and clearance required for the robot")
    print(">> Example: if point is (x=2, y=5), then your input should be '2 5'")
    
    init_pos_str = input("Initial position: ")
    target_pos_str = input("Target position: ")
    radius_str = input("Robot radius: ")
    clearance_str = input("Clearance required: ")
    
    is_input_valid = True
    try:
        init_pos = [int(coord) for coord in init_pos_str.split()]
        target_pos = [int(coord) for coord in target_pos_str.split()]
        robot_radius = int(radius_str)
        clearance_req = int(clearance_str)

        if len(init_pos) != 2 or len(target_pos) != 2:
            raise Exception("Invalid input")

    except:
        is_input_valid = False
        print('Invalid input. Try again!')

    if is_input_valid:
        init_pos = init_pos[1], init_pos[0]
        target_pos = target_pos[1], target_pos[0]

        c_space = ConfigurationSpace(height=200, width=300, radius_of_bot=robot_radius, clearance=clearance_req)
        c_space_map = c_space.get_cspace_map()

        path_explorer = PathExplorer()
        path_explorer.find_path(init_pos, target_pos, c_space_map)

        

     

