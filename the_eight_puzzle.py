from collections import deque

# A* with the Misplaced Tile heuristic
def misplaced_tiles_heuristic(state, end):
    misplaced_tiles = sum(1 for i in range(9) if state[i] != '0' and state[i] != end[i])
    return misplaced_tiles

def A_star_with_Misplaced_Tile(start, end, queue, distance, parent):
    queue.append(start)
    distance[start] = 0
    parent[start] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        queue = deque(sorted(queue, key=lambda x: distance[x] + misplaced_tiles_heuristic(x, end)))
        tile = queue.popleft()
        dist = distance[tile]  # Fixing variable name to avoid conflict
        if tile == end:
            return dist
        k = tile.find('0')
        x = k // 3
        y = k % 3
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < 3 and 0 <= b < 3:
                father = tile
                tile_list = list(tile)
                tile_list[k], tile_list[a * 3 + b] = tile_list[a * 3 + b], tile_list[k]
                new_tile = ''.join(tile_list)
                if new_tile not in parent:
                    parent[new_tile] = father
                if new_tile not in distance:
                    distance[new_tile] = dist + 1  # Use new_tile instead of tile
                    queue.append(new_tile)
    return -1

# Uniform Cost Search
def uniform_cost_search(start, end, queue, distance, parent):
    queue.append(start)
    distance[start] = 0
    parent[start] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        tile = queue.popleft()
        dist = distance[tile]  # Fixing variable name to avoid conflict
        if tile == end:
            return dist
        k = tile.find('0')
        x = k // 3
        y = k % 3
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < 3 and 0 <= b < 3:
                father = tile
                tile_list = list(tile)
                tile_list[k], tile_list[a * 3 + b] = tile_list[a * 3 + b], tile_list[k]
                new_tile = ''.join(tile_list)
                if new_tile not in parent:
                    parent[new_tile] = father
                if new_tile not in distance:
                    distance[new_tile] = dist + 1  # Use new_tile instead of tile
                    queue.append(new_tile)
    return -1

# A* with the Manhattan Distance heuristic
def manhattan_distance_heuristic(state, end):
    md = sum(abs(i // 3 - int(state[i]) // 3) + abs(i % 3 - int(state[i]) % 3) for i in range(9) if state[i] != '0')
    return md

def A_star_with_Manhattan_Distance(start, end, queue, distance, parent):
    queue.append(start)
    distance[start] = 0
    parent[start] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        queue = deque(sorted(queue, key=lambda x: distance[x] + manhattan_distance_heuristic(x, end)))
        tile = queue.popleft()
        dist = distance[tile]  # Fixing variable name to avoid conflict
        if tile == end:
            return dist
        k = tile.find('0')
        x = k // 3
        y = k % 3
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < 3 and 0 <= b < 3:
                father = tile
                tile_list = list(tile)
                tile_list[k], tile_list[a * 3 + b] = tile_list[a * 3 + b], tile_list[k]
                new_tile = ''.join(tile_list)
                if new_tile not in parent:
                    parent[new_tile] = father
                if new_tile not in distance:
                    distance[new_tile] = dist + 1  # Use new_tile instead of tile
                    queue.append(new_tile)
    return -1

def solve_puzzle(matrix):
    start = ''.join(str(elem) for row in matrix for elem in row)
    end = '123456780'
    queue = deque()
    distance = {}
    parent= {}
    print("A* with Misplaced Tile Heuristic:")
    res_misplaced = A_star_with_Misplaced_Tile(start, end, queue, distance, parent)
    if res_misplaced != -1:
        print('Shortest Steps:', res_misplaced)
        formal = parent[end]
        path = [end]
        while formal:
            path.append(formal)
            formal = parent[formal]
        path.reverse()

        for i in range(res_misplaced + 1):
            for a in range(3):
                print(path[i][a], end=' ')
            print('')
            for a in range(3):
                print(path[i][a + 3], end=' ')
            print('')
            for a in range(3):
                print(path[i][a + 6], end=' ')
            print('')
            print('')

        print('Goal state arrived!')
        print('Expanded nodes:', len(parent))
    else:
        print("It could not be solved!")

    print("\nUniform Cost Search:")
    queue.clear()
    distance.clear()
    parent.clear()
    res_uniform = uniform_cost_search(start, end, queue, distance, parent)
    if res_uniform != -1:
        print('Shortest Steps:', res_uniform)
        print('Expanded nodes:', len(parent))
    else:
        print("It could not be solved!")

    print("\nA* with Manhattan Distance Heuristic:")
    queue.clear()
    distance.clear()
    parent.clear()
    res_manhattan = A_star_with_Manhattan_Distance(start, end, queue, distance, parent)
    if res_manhattan != -1:
        print('Shortest Steps:', res_manhattan)
        print('Expanded nodes:', len(parent))
    else:
        print("It could not be solved!")

# Input
def get_input():
    matrix = []
    for i in range(3):
        input_str = input(f"Please enter the {i+1} row of the matrix with '1 2 3' format: ")
        row = [int(num) for num in input_str.split()]
        matrix.append(row)
    return matrix

def main():
    matrix = get_input()
    print("Matrix:", matrix)
    solve_puzzle(matrix)

if __name__ == "__main__":
    main()
