import traceback
from constants import *

def receive_inputs():
    #print(">> Bottom left corner is considered as (0,0)")
    
    print(">> Enter the initial and target positions (within -5 to 5mtr), initial orientation, clearance, and two wheel rpms required for the robot")
    print(">> Example: if point is (x=2, y=5), then your input should be '2 5'")
    print(">> if rpm is (rpm1=10, rpm2=20), then your input should be '10 20'")
    
    init_pos_str = input("Initial position (x y): ")
    orientation_str = input("Initial Orientation (in degrees): ")
    target_pos_str = input("Target position (x y): ")
    rpms_str = input("Speed of the wheels in RPM (RPM1 RPM2): ")
    clearance_str = input("Clearance required (in meters, recommended: 0 to 0.35m): ")
    
    is_input_valid = True
    
    try:
        init_pos = [float(coord) for coord in init_pos_str.split()]
        target_pos = [float(coord) for coord in target_pos_str.split()]
        orientation = float(orientation_str)
        wheel_vels = [(TWO_PI/60) * float(rpm) for rpm in rpms_str.split()]
        clearance_req = float(clearance_str)

        if len(init_pos) != 2 or len(target_pos) != 2 or len(wheel_vels) != 2:
            raise Exception("Invalid input")

    except:
        is_input_valid = False
        traceback.print_exc()
        print('Invalid input. Try again!')
        return is_input_valid, None, None, None, None, None
    
    return is_input_valid, init_pos, target_pos, orientation, clearance_req, wheel_vels

if __name__ == "__main__":
    receive_inputs()