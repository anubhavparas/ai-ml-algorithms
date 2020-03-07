
def receive_inputs(is_robot_rigid):
    print(">> Bottom left corner is considered as (0,0)")
    if is_robot_rigid:
        print(">> Enter the initial and target positions, radius and clearance required for the robot")
    else:
        print(">> Enter the initial and target positions of the robot")
    print(">> Example: if point is (x=2, y=5), then your input should be '2 5'")
    
    init_pos_str = input("Initial position: ")
    target_pos_str = input("Target position: ")
    
    radius_str = '0'
    clearance_str = '0'
    if is_robot_rigid:
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
    
    return is_input_valid, init_pos, target_pos, robot_radius, clearance_req