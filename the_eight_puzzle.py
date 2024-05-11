from collections import deque
from queue import PriorityQueue

# Heuristic function for the Misplaced Tile heuristic
def misplaced_tiles_heuristic(state, end):
    misplaced_tiles = sum(1 for i in range(9) if state[i] != '0' and state[i] != end[i])
    return misplaced_tiles

# A* algorithm with the Misplaced Tile heuristic
def A_star_with_Misplaced_Tile(start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))  # Initialize priority queue with the start state and priority 0
    came_from = {start: None}  # Initialize dictionary to store parent states
    g_score = {start: 0}  # Initialize dictionary to store the cost from start to each state
    expanded_nodes = 0  # Track the number of expanded nodes
    
    while not open_set.empty():
        _, current = open_set.get()  # Get the state with the smallest priority (distance + heuristic)
        expanded_nodes += 1  # Increment the count of expanded nodes
        
        if current == end:
            return g_score[current], came_from, expanded_nodes  # If the goal state is reached, return the distance, parent dictionary, and expanded nodes
        
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1  # Cost of current path plus one step
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                priority = tentative_g_score + misplaced_tiles_heuristic(neighbor, end)
                open_set.put((priority, neighbor))  # Add the neighbor state to the priority queue with priority based on f = g + h
    
    return -1

# Function to get neighboring states
def get_neighbors(state):
    neighbors = []
    zero_index = state.index('0')
    x, y = zero_index // 3, zero_index % 3
    
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(''.join(new_state))
    
    return neighbors

from queue import PriorityQueue

# Uniform Cost Search
def uniform_cost_search(start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))  # Initialize priority queue with the start state and priority 0
    distance = {start: 0}  # Initialize dictionary to store the distance from start to each state
    parent = {start: None}  # Initialize dictionary to store parent states
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    expanded_nodes = 0  # Track the number of expanded nodes
    
    while not open_set.empty():
        _, tile = open_set.get()  # Get the state with the smallest priority (distance)
        expanded_nodes += 1  # Increment the count of expanded nodes
        
        if tile == end:
            return distance[tile], expanded_nodes  # If the goal state is reached, return the distance and expanded nodes
        
        k = tile.index('0')
        x = k // 3
        y = k % 3
        
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < 3 and 0 <= b < 3:
                new_tile = swap(tile, k, a * 3 + b)  # Generate new state by swapping '0' tile with its neighbor
                new_distance = distance[tile] + 1  # Increment the distance by 1
                
                if new_tile not in parent or new_distance < distance[new_tile]:
                    parent[new_tile] = tile
                    distance[new_tile] = new_distance
                    open_set.put((new_distance, new_tile))  # Add the neighbor state to the priority queue with priority based on distance
    
    return -1

# Function to swap elements in a string at given indices
def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


# Manhattan distance heuristic function
def manhattan_distance_heuristic(state, end):
    md = sum(abs(i // 3 - end.index(state[i]) // 3) + abs(i % 3 - end.index(state[i]) % 3) for i in range(9) if state[i] != '0')
    return md

# A* algorithm with Manhattan Distance heuristic
def A_star_with_Manhattan_Distance(start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))  # Initialize priority queue with start state and priority 0
    came_from = {start: None}  # Initialize dictionary to store parent states
    g_score = {start: 0}  # Initialize dictionary to store the cost from start to each state
    expanded_nodes = 0  # Track the number of expanded nodes
    
    while not open_set.empty():
        _, current = open_set.get()  # Get the state with the smallest priority (distance + heuristic)
        expanded_nodes += 1  # Increment the count of expanded nodes
        
        if current == end:
            return g_score[current], expanded_nodes  # If the goal state is reached, return the cost and expanded nodes
        
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1  # Cost of current path plus one step
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                priority = tentative_g_score + manhattan_distance_heuristic(neighbor, end)
                open_set.put((priority, neighbor))  # Add the neighbor state to the priority queue with priority based on f = g + h
    
    return -1

# Function to get neighboring states
def get_neighbors(state):
    neighbors = []
    zero_index = state.index('0')
    x, y = zero_index // 3, zero_index % 3
    
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(''.join(new_state))
    
    return neighbors

def solve_puzzle(matrix):
    start = ''.join(str(elem) for elem in matrix)
    end = '123456780'
    print("A* with Misplaced Tile Heuristic:")
    res_misplaced, parent_misplaced, expanded_misplaced = A_star_with_Misplaced_Tile(start, end)
    if res_misplaced != -1:
        print('Shortest Steps:', res_misplaced)
        print('Expanded nodes:', expanded_misplaced)
    else:
        print("It could not be solved!")

    print("\nUniform Cost Search:")
    res_uniform, expanded_uniform = uniform_cost_search(start, end)
    if res_uniform != -1:
        print('Shortest Steps:', res_uniform)
        print('Expanded nodes:', expanded_uniform)
    else:
        print("It could not be solved!")

    print("\nA* with Manhattan Distance Heuristic:")
    res_manhattan, expanded_manhattan = A_star_with_Manhattan_Distance(start, end)
    if res_manhattan != -1:
        print('Shortest Steps:', res_manhattan)
        print('Expanded nodes:', expanded_manhattan)
    else:
        print("It could not be solved!")

# Input
def get_input():
    input_str = input("Enter the rows of the matrix in the format 1 2 3, 4 5 6, 0 7 8: ")
    matrix = [int(num) for row in input_str.split(',') for num in row.split()]
    return matrix

def main():
    matrix = get_input()
    print("Matrix:", matrix)
    solve_puzzle(matrix)

if __name__ == "__main__":
    main()
