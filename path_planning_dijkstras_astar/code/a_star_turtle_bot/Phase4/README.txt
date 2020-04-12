This is the catkin package to implement simulation.

It is assumed that the following pakcages and softwares are already installed in your system:
- ROS
- Gazebo
- Turtlebot3

The package 'simulate_robot' contains the following folders:
- launch 
- src
- scripts
- worlds
- CMakeLists.txt
- package.xml

Ensure that your package as all these files in place.
It is required that you have catkin_ws in place, if not, 
$ mkdir catkin_ws $
$ catkin_make $
Copy the package 'simulate_robot' in catkin_ws/src
$ cd ~/catkin_ws $
$ catkin_make $
$ source devel/setup.bash $

The Launch folder contains the environment launch file 'phase4_map.launch'
To spawn the robot (Turtlebot3 ; MODEL:=burger) in the map given (map.world - you can find this in the worlds folder) execute - 

$ roslaunch simulate_robot phase4_map.launch x_pos:=-4.0 y_pos:=-3.0 yawn:=0.349 $

Arguments to this launch file: x_pos:=(x coordinate postion), y_pos:=(y coordinate position), yawn:=(initial orientation in radians)

Please note, the initial pose of the robot must be the same as that entered when executing $ python3 a_star_rigid.py $, However, initial orientation is to be given in radians here and not in degrees

Before launching this ROS file, we need to execute the planner (similar to Phase 3):
$ cd ~/Phase3/code/ $
$ python3 a_star_rigid.py $

Once execution is complete,
Go to the 'params' folder in 'Phase3' to retrieve the .json file saved. Load the location of this file into the ROS publisher code - velocity_publisher.py
You can find velocity_publisher.py in 

$ cd ~/catkin_ws/src/simulate_robot/scripts/ $

Change the file path argument in 'file_name' , it is mentioned in the code
Now, open a new terminal, and execute:

Please ensure, appropriate file path is entered
$ rosrun simulate_robot velocity_publisher.py $

This should simulate the robot in ROS environment
