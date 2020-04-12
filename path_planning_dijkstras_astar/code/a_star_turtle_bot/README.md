# Path planning using A* Algorithm for differential drive robot with non-holonomic constraints

#### The problem statement is to find the shortest path in terms of cost for a rigid robot to reach from one point to a target position in a 2-D map comprising of obstacles.

##### Following are the instructions to run the code:
- Make sure you have the following files in the same directory location:
   1) configurationspace.py
   2) cspaceplotter.py
   3) pathexplorer.py
   4) simplepriorityqueue.py
   5) msgs.txt
   6) robot.py
   7) input_receiver.py
   8) heuristics.py
   9) a_star_rigid.py
  10) obstacle_check.py
  11) constants.py
  12) curveplotter.py
- In the terminal where you can run python scripts go to the directory where the above files are located
- Make sure you have numpy installed. *[help](https://docs.scipy.org/doc/numpy/user/install.html)*
- For testing rigid robot: Type: **$ python a_star_rigid.py**

##### The configuration space is given as follows:
Defining the configuration space

Configuration space for point robot, when both radius and clearance are 0 units

![alt text](./media/c_space00.PNG?raw=true "Configuration Space for Point Robot")

Configuration space for rigid robot, with radius=0.177m and clearance=0.4m defined by the user

![alt text](./media/c_space.PNG?raw=true "Configuration Space for Rigid Robot")


##### Sample input-output case scenarios:

The goal threshold radius is set to 0.2m

-- Few sample inputs are:

###Sample 1:

Initial position (x y): -4 -3

Initial Orientation (in degrees): 30

Target position (x y): 0 -3

Speed of the wheels in RPM (RPM1 RPM2): 70 80

Clearance required (in meters, recommended: 0 to 0.35m): 0.3

Time taken: 2.2881642000000006 seconds(approx: 0 min: 2 sec)

Cost of the path:  6.997897635871265 units



###Sample 2:

Initial position (x y): -4 -4

Initial Orientation (in degrees): 60

Target position (x y): 4 2

Speed of the wheels in RPM (RPM1 RPM2): 70 80

Clearance required (in meters, recommended: 0 to 0.35m): 0.3

Time taken: 4.9481258 seconds(approx: 0 min: 4 sec)

Cost of the path:  15.550883635269475 units



###Sample 3:

Initial position (x y): -4.5 -4.5

Initial Orientation (in degrees): 120

Target position (x y): 2 0

Speed of the wheels in RPM (RPM1 RPM2): 140 10

Clearance required (in meters, recommended: 0 to 0.35m): 0

Time taken: 3.0584932999999985 seconds(approx: 0 min: 3 sec)

Cost of the path:  7.809475738048622 units


