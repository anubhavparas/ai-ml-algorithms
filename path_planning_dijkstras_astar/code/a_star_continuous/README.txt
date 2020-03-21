# Path planning using A* Algorithm

#### The problem statement is to find the shortest path in terms of cost for a point and rigid robot to reach from one point to a target position in a 2-D map comprising of obstacles.

##### Following are the instructions to run the code:
- Make sure you have the following files in the same directory location:
   1) configurationspace.py
   2) cspaceplotter.py
   3) pathexplorer.py
   4) simplepriorityqueue.py
   5) msgs.txt
   6) cspacepredicatesupplier.py
   7) input_receiver.py
   8) heuristics.py
   9) a_star_rigid.py
  10) obstacle_check.py
- In the terminal where you can run python scripts go to the directory where the above files are located
- Make sure you have numpy installed. *[help](https://docs.scipy.org/doc/numpy/user/install.html)*
- For testing rigid robot: Type: **$ python a_star_rigid.py**

##### Sample input-output case scenarios:
Angle between actions (here, theta) is considered as 30 deg.
The goal threshold radius is set to 1.5

- For Rigid robot:

  **Input:**
  - Initial position: 50 30
  - Initial orientation: 60
  - Target position: 150 150
  - Step Size: 1
  - Robot Radius: 1
  - Clearance Required: 1

  **Output:**
  - Time take: 616.05278529999996 sec
  - Cost of the path: 377.487373415293 units

