import cv2
import numpy as np
import math
from queue import Queue, deque
import time
import matplotlib.pyplot as plt
from simplepriorityqueue import SimplePriorityQueue
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from cspaceplotter import CSpacePlotter
from constants import *
from curveplotter import plot_curve
import json
from videowriter import write_video


class PathExplorer:
    def find_path(self, initial_pos, target_pos, orientation, wheel_vels, t_bot, c_space, heuristic_func, action_angle=30):
        initial_pos = (initial_pos[0], initial_pos[1])
        target_pos = (target_pos[0], target_pos[1])
        
        
        if (not self.is_position_valid(initial_pos, c_space)) or (not self.is_position_valid(target_pos, c_space)):
            print("Either initial or target position lies in the obstacle space or out of the configuration space. Please check and try again.")
            return

        node_queue = SimplePriorityQueue()
        visited_nodes_set = set()
        visited_nodes_list = []
    
        initial_node = {
            'pos': initial_pos,
            'orientation': orientation,
            'path': [],
            'parent': None,
            'cost': 0, 
            'cost_to_go': heuristic_func(initial_pos, target_pos)
            }

        action_velocity_list = self.get_linear_and_ang_vel(t_bot, wheel_vels)

        cost_update_map = {}
        cost_update_map[self.get_rounded_pos_orient(initial_node)] = 0

        is_target_found = False

        # cost to reach to the node as a key to sort
        node_queue.put(0, initial_node)

        msg_queue = Queue()
        self.init_msg_queue(msg_queue)
        count = 0
        print('Starting path exploration...')
        start = time.clock()
        while (not node_queue.isempty()) and not is_target_found:
            count +=  1
            if (not msg_queue.empty()) and (count % 5000 == 0):
                print(msg_queue.get())
            
            current_node = node_queue.get()[1]
            node_pos_orient = self.get_rounded_pos_orient(current_node)
            #if node_pos_orient not in visited_nodes_set:
            visited_nodes_list.append(current_node)
            visited_nodes_set.add(node_pos_orient)

            if self.is_within_goal_region(current_node['pos'], target_pos):
                print('\nTarget found')
                is_target_found = True
                solution_path, path_cost = current_node['path'], current_node['cost'] 
            else:
                next_positions = self.get_next_positions(current_node, c_space, target_pos, action_velocity_list, t_bot, heuristic_func)
                for node in next_positions:
                    rounded_child = self.get_rounded_pos_orient(node)
                    if rounded_child not in visited_nodes_set:
                        old_cost_for_node = math.inf if rounded_child not in cost_update_map.keys() else cost_update_map[rounded_child]
                        new_cost_for_node = node['cost'] + node['cost_to_go']
                        if old_cost_for_node > new_cost_for_node:
                            cost_update_map[rounded_child] = node['cost']
                            node_queue.put(new_cost_for_node, node)

        end = time.clock()

        print('Time taken:', end-start, 'seconds(approx:', int((end-start)/60),'min:', int((end-start)%60), 'sec)' )
        if is_target_found:
            print('Cost of the path: ', path_cost, 'units')
            path_params = self.write_param_json(solution_path, (initial_pos[1], initial_pos[0], orientation))
            self.start_visualization(initial_node, target_pos, visited_nodes_list, solution_path, path_cost, c_space, t_bot)
            return path_params
        else:
            print('Target cannot be reached')

        
    def is_within_goal_region(self, position, target_pos, goal_threshold_radius=GOAL_THRESH):
        return math.sqrt((target_pos[0]-position[0])**2 + (target_pos[1]-position[1])**2) <= goal_threshold_radius

    def get_rounded_pos_orient(self, node, pos_threshold=0.1, orientation_threshold=30):
        node_pos_y, node_pos_x = node['pos']
        orientation = node['orientation']
        node_pos_x = self.roundoff_value(node_pos_x, pos_threshold)
        node_pos_y = self.roundoff_value(node_pos_y, pos_threshold)
        orientation = self.roundoff_value(orientation, orientation_threshold)

        return (node_pos_x, node_pos_y, orientation)

    def roundoff_value(self, value, roundoff_threshold):
        return (round(value/roundoff_threshold))*roundoff_threshold

    def get_next_positions(self, node, c_space, target_pos, action_velocity_list, t_bot, heuristic_func):
        next_postions = []
        
        node_pos = list(node['pos'])
        for ind, velocity in enumerate(action_velocity_list):
            next_pos, next_orient = self.get_new_pose(velocity[LIN], velocity[ANG], node_pos, node['orientation'], c_space)

            if next_pos is not None:
                node_path = node['path'].copy()
                node_path.append(velocity)
                
                next_postions.append({
                    'pos': tuple(next_pos),
                    'orientation': next_orient,
                    'path': node_path,
                    'parent': (node['pos'], node['orientation']),
                    'cost': node['cost'] + (velocity[LIN] * delta_t),
                    'cost_to_go': heuristic_func(next_pos, target_pos)
                })
        return next_postions
    
    def get_linear_and_ang_vel(self, t_bot, wheel_vels):
        omega_1, omega_2 = wheel_vels[0], wheel_vels[1]
        omega_combinations = [
            [0, omega_1],
            [omega_1, 0],
            [omega_1, omega_1],
            [0, omega_2],
            [omega_2, 0],
            [omega_2, omega_2],
            [omega_1, omega_2],
            [omega_2, omega_1]
        ]
        velocity_list = []
        for omega in omega_combinations:
            linear_v = 0.5*t_bot.wheel_rad * (omega[L] + omega[R])
            angular_v = (t_bot.wheel_rad/t_bot.dist_bet_wheels) * (omega[R] - omega[L])
            velocity_list.append([linear_v, angular_v])
        return velocity_list

    def get_new_pose(self, linear_v, angular_v, node_pos, orientation, c_space):
        x, y = node_pos[1], node_pos[0]
        orient_rad = math.radians(orientation)
        t = 0
        dt = delta_t/10 #0.1
        while t <= delta_t:
            t = t + dt
            x += linear_v * math.cos(orient_rad) * dt
            y += linear_v * math.sin(orient_rad) * dt
            if c_space.is_point_in_obstacle(x, y):
                return None, None
            orient_rad += angular_v * dt
        orientation = self.adjust_angle(orient_rad)
        return np.array([y, x]), orientation
    

    def adjust_angle(self, orientation):
        orientation = math.degrees(orientation)
        if orientation < 0:
            orientation = 360 + orientation
        elif orientation >= 360:
            orientation = orientation % 360
        return orientation

    def is_position_valid(self, position, c_space):
        return not c_space.is_point_in_obstacle(position[1], position[0])


    def start_visualization(self, initial_node, target_pos, visited_nodes, path, path_cost, c_space, t_bot):
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')

        fig, ax = plt.subplots()
        plt.xlim(c_space.x_limit[0]-0.1, c_space.x_limit[1]+0.1)
        plt.ylim(c_space.y_limit[0]-0.1, c_space.y_limit[1]+0.1)

        plt.grid()
        ax.set_aspect('equal')

        # small circle of GOAL_THRESH unit radius to mark the goal region
        a_circle = plt.Circle((target_pos[1], target_pos[0]), GOAL_THRESH)
        ax.add_artist(a_circle)

        cmap_plotter = CSpacePlotter(c_space)
        cmap_plotter.plotMap(fig, ax)
        
        dots = {0: '    ', 1: '.   ', 2: '..  ', 3: '... ', 4: '....'} 
        num_dots = len(dots)
        
        print('Visualization in process...\n')
        out = cv2.VideoWriter("./media/astar_nonholonomic.mp4", fourcc, 1.0, (509, 524))
        print(len(visited_nodes))
        sample_num = 100
        def animate(i):
            if i < len(visited_nodes):
                
                ax.set_title('Exploring Configuration Space' + str(dots[i%num_dots]), fontsize=13)
                if len(visited_nodes[i]['path']) != 0:
                    
                    parent_pos = visited_nodes[i]['parent']
                    parent_y, parent_x = parent_pos[0]
                    velocity = visited_nodes[i]['path'][-1]
                    orientation = parent_pos[1]
                    plot_curve(ax, (parent_x, parent_y), orientation, velocity, t_bot, 'orange')
                    #print(i, len(visited_nodes))
                    if (i % sample_num == 0):
                        plt.savefig('./media/frame'+str(i)+'.png', bbox_inches='tight')
                        #frame = cv2.imread('./media/frame'+str(i)+'.png')
                        #print(frame.shape)
                        #out.write(frame)
            else:
                goal_reached_str = 'Goal Reached. Cost: ' + str(path_cost) + 'units' 
                ax.set_title(goal_reached_str, fontsize=13)
                
                position, orient = list(initial_node['pos']), initial_node['orientation']
                y_pos, x_pos = position[0], position[1]
                for action in path:
                    x_pos, y_pos, orient = plot_curve(ax, (x_pos, y_pos), orient, action, t_bot, 'blue')
                    
                #'''
                plt.savefig('./media/frame.png', bbox_inches='tight')
                #frame = cv2.imread('./media/frame.png')
                #out.write(frame)
                #'''
            
            
        #out.release()
        '''
        for i in range(len(visited_nodes)):
            ax.set_title('Exploring Configuration Space' + str(dots[i%num_dots]), fontsize=13)
            if len(visited_nodes[i]['path']) != 0:
                
                parent_pos = visited_nodes[i]['parent']
                parent_y, parent_x = parent_pos[0]
                velocity = visited_nodes[i]['path'][-1]
                orientation = parent_pos[1]
                plot_curve(ax, (parent_x, parent_y), orientation, velocity, t_bot, 'orange')
                #print(visited_nodes[i])
                print(i, len(visited_nodes))
                
                if (i % sample_num == 0):
                    plt.savefig('./media/frame'+str(i)+'.png', bbox_inches='tight')
                    #frame = cv2.imread('./media/frame'+str(i)+'.png')
                    #print(frame.shape)
                    #out.write(frame)
        
        goal_reached_str = 'Goal Reached. Cost: ' + str(path_cost) + 'units' 
        ax.set_title(goal_reached_str, fontsize=13)
        
        position, orient = list(initial_node['pos']), initial_node['orientation']
        y_pos, x_pos = position[0], position[1]
        for action in path:
            x_pos, y_pos, orient = plot_curve(ax, (x_pos, y_pos), orient, action, t_bot, 'blue')
        plt.savefig('./media/frame.png', bbox_inches='tight')
        '''
        anim = FuncAnimation(fig, animate, frames=len(visited_nodes)+1, interval=0.01, blit=False, repeat=False)
        
        #out.release()
        fig.show()
        plt.draw()
        plt.show()
        out.release()

        #anim.save('./media/a_star_exploration.gif', writer='imagepick', fps=60)
        #out.release()
        write_video((len(visited_nodes)), sample_num)

        print('\nVisualization Complete.')
    
    def write_param_json(self, action_path, init_pose):
        params_data = {}
        params_data['velocity'] = list(action_path)
        params_data['delta_time'] = delta_t
        params_data['init_pose'] = init_pose

        file_name = 'params/action_velocity.json'
        with open(file_name, 'w') as outfile:
            json.dump(params_data, outfile)
        return params_data

    
    def init_msg_queue(self, msg_queue):
        with open('msgs.txt', 'r') as msg_file:
            msg_queue.queue = deque(msg_file.readlines())
