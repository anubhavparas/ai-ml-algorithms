import cv2
import numpy as np
import math
from queue import Queue, deque
import time
from simplepriorityqueue import SimplePriorityQueue


class PathExplorer:
    
    def find_path(self, initial_pos, target_pos, cspace_map):

        matrix_dim_row, matrix_dim_col = cspace_map.shape[0], cspace_map.shape[1]
        initial_pos = (matrix_dim_row-1 - initial_pos[0], initial_pos[1])
        target_pos = (matrix_dim_row-1 - target_pos[0], target_pos[1])
        
        if (not self.is_position_valid(initial_pos, cspace_map)) or (not self.is_position_valid(target_pos, cspace_map)):
            print("The initial or target positions lie in the obstacle space or out of the configuration space. Please check and try again.")
            return

        cost_matrix = np.zeros((matrix_dim_row, matrix_dim_col), dtype=object)
        cost_matrix[:, :] = math.inf

        node_queue = SimplePriorityQueue()
        visited_nodes_set = set()
        visited_nodes_list = []
        

        initial_node = {'pos': initial_pos, 'path': [], 'cost': 0}
        cost_matrix[initial_pos] = 0


        is_target_found = False

        # cost to reach to the node as a key to sort
        node_queue.put(0, initial_node)

        msg_queue = Queue()
        self.init_msg_queue(msg_queue)
        count = 0
        start = time.clock()
        while (not node_queue.isempty()) and not is_target_found:
            count +=  1
            if (not msg_queue.empty()) and (count % 15000 == 0):
                print(msg_queue.get())
            
            current_node = node_queue.get()[1]
            if current_node['pos'] == target_pos:
                print('\n\nTarget found')
                is_target_found = True
                solution_path, path_cost = current_node['path'], current_node['cost'] 
            else:
                visited_nodes_list.append(current_node['pos'])
                visited_nodes_set.add(current_node['pos'])
                next_positions = self.get_next_positions(current_node, cspace_map)
                for node in next_positions:
                    if node['pos'] not in visited_nodes_set:
                        old_cost_to_reach_node = math.inf if cost_matrix[node['pos']] == math.inf else cost_matrix[node['pos']]['cost'] 
                        new_cost_to_reach_node = node['cost']
                        if old_cost_to_reach_node > new_cost_to_reach_node:
                            cost_matrix[node['pos']] = node
                            node_queue.put(node['cost'], node)

        end = time.clock()

        print('Time taken:', end-start, 'seconds')
        if is_target_found:
            print('Cost of the path: ', path_cost, 'units')
            #print(solution_path)
            self.start_visualization(initial_pos, visited_nodes_list, solution_path, cspace_map)
        else:
            print('Target cannot be reached')

        
        
    def get_next_positions(self, node, cspace_map):
        ## add the cache logic
        
        ## for a 2D matrix (0,0) is there at the top left corner
        actions = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1], 
                'UL': [-1, -1], 'UR': [-1, 1], 'DL': [1, -1], 'DR': [1, 1]}
        
        ROOT_TWO = math.sqrt(2)
        action_cost_map = {
            'U': 1, 'D': 1, 'L': 1, 'R': 1, 
            'UL': ROOT_TWO, 'UR': ROOT_TWO, 'DL': ROOT_TWO, 'DR': ROOT_TWO}
        
        next_postions = []
        
        node_pos = list(node['pos'])
        for action in actions:
            next_pos = np.add(node_pos, actions[action])
            if self.is_position_valid(next_pos, cspace_map):
                node_path = node['path'].copy()
                node_path.append(action)
                
                next_postions.append({
                    'pos': tuple(next_pos),
                    'path': node_path,
                    'cost': node['cost'] + action_cost_map[action]
                })
        return next_postions
                
        
    def is_position_valid(self, position, cspace_map):
        BLUE = (255, 0, 0)
        point_not_in_obstacle_area = False
        if (position[0] in range(0, cspace_map.shape[0]) and position[1] in range(0, cspace_map.shape[1])):
            point_not_in_obstacle_area = not (tuple(cspace_map[position[0], position[1]]) == BLUE)
        
        return point_not_in_obstacle_area

    
    def start_visualization(self, initial_pos, visited_nodes, path, cspace_map):
        try:
            WHITE = (255,255,255)
            GREEN = (0,255,0)
            cspace_map[initial_pos] = WHITE
            cv2.imshow('Environment Map', cspace_map)
            actions = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1], 
                    'UL': [-1, -1], 'UR': [-1, 1], 'DL': [1, -1], 'DR': [1, 1]}

            initial_pos = list(initial_pos)
            print('Visualization in process...\nPress Esc key to stop.')
            for node in visited_nodes:
                cspace_map[node] = WHITE
                cv2.imshow('Environment Map', cspace_map)
                if cv2.waitKey(1) == 27:
                    break

            next_pos = initial_pos
            for action in path:
                next_pos = np.add(next_pos, actions[action])
                cspace_map[tuple(next_pos)] = GREEN
            
            cv2.imshow('Environment Map', cspace_map)
            print('\nVisualization Complete. Press Esc key to exit.')
        except:
            print("Something went wrong in visualization.")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
    def init_msg_queue(self, msg_queue):
        with open('msgs.txt', 'r') as msg_file:
            msg_queue.queue = deque(msg_file.readlines())


