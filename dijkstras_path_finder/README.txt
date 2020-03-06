# Path planning using Dijkstra's Algorithm

#### The problem statement is to find the shortest path in terms of cost for a point and rigid robot to reach from one point to a target position in a 2-D map comprising of obstacles.

##### Following are the instructions to run the code:
- Make sure you have the following files in the same directory location:
   1) configurationspace.py
   2) dijkstra_point.py
   3) dijkstra_rigid.py
   4) pathexplorer.py
   5) simplepriorityqueue.py
   6) msgs.txt
   7) cspacepredicates.py
   8) input_receiver.py
   9) heuristics.py
  10) a_star_point.py
  11) a_star_rigid.py
- In the terminal where you can run python scripts go to the directory where the above files are located
- Make sure you have numpy installed. *[help](https://docs.scipy.org/doc/numpy/user/install.html)*
- For testing point robot:  Type: **$ python dijkstra_point.py**
- For testing rigid robot:  Type: **$ python dijkstra_rigid.py**
- Follow the input instructions that will appear once the scripts are executed.
- To execute the same map using a-star algorithm execute the following commands:
- For testing point robot: Type: **$ python a_star_point.py**
- For testing rigid robot: Type: **$ python a_star_rigid.py**

##### Sample input test cases:
For point robot, following test cases may be checked,
Initial position : 0 0 / 1 1 / 2 5 / 4 4 / 199 199 / 5 5 
Target position : 199 199 / 100 100 / 120 120 / 150 150 / 0 0 / 295 195

For rigid robot, following test cases may be checked,
Initial position: 16 16 / 6 6 / 3 3 / 5 5
Target position : 140 178 / 150 150 / 140 160 / 295 195
Robot Radius : 5 / 2 / 1 / 1
Clearance Required : 6 / 3 / 1 / 1

##### Sample input-output case scenarios:
- For Point Robot:
INPUT:
Initial position: 5 5
Target position: 295 195

OUTPUT:
Time taken: 31.0661988 sec
Cost of the path: 375.7300141024123 units

- For Rigid robot:
INPUT:
Initial position: 5 5
Target position: 295 195
Robot Radius: 1
Clearance Required: 1

OUTPUT:
Time take: 29.05278529999996 sec
Cost of the path: 377.487373415293 units
