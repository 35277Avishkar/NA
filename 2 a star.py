from heapq import heappop, heappush


class Node:
    def __init__(self, state, g_cost, h_cost, parent=None):
        self.state = state
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost


def heuristic(state, goal_state):
    # Manhattan distance heuristic
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                value = state[i][j]
                goal_position = divmod(value - 1, 3)
                distance += abs(goal_position[0] - i) + abs(goal_position[1] - j)
    return distance


def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_successor_states(state):
    i, j = get_blank_position(state)
    successors = []

    # Move blank space left
    if j > 0:
        successor = [row[:] for row in state]
        successor[i][j], successor[i][j - 1] = successor[i][j - 1], successor[i][j]
        successors.append(successor)

    # Move blank space right
    if j < 2:
        successor = [row[:] for row in state]
        successor[i][j], successor[i][j + 1] = successor[i][j + 1], successor[i][j]
        successors.append(successor)

    # Move blank space up
    if i > 0:
        successor = [row[:] for row in state]
        successor[i][j], successor[i - 1][j] = successor[i - 1][j], successor[i][j]
        successors.append(successor)

    # Move blank space down
    if i < 2:
        successor = [row[:] for row in state]
        successor[i][j], successor[i + 1][j] = successor[i + 1][j], successor[i][j]
        successors.append(successor)

    return successors


def astar_search(start_state, goal_state):
    open_list = []
    closed_list = set()

    # Create the initial node
    initial_node = Node(start_state, 0, heuristic(start_state, goal_state), None)
    heappush(open_list, initial_node)

    while open_list:
        current_node = heappop(open_list)
        current_state = current_node.state

        if current_state == goal_state:
            # Goal state reached, return the path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))

        closed_list.add(tuple(map(tuple, current_state)))

        # Generate successor states
        successors = get_successor_states(current_state)

        for successor_state in successors:
            g_cost = current_node.g_cost + 1
            h_cost = heuristic(successor_state, goal_state)
            successor_node = Node(successor_state, g_cost, h_cost, current_node)

            if tuple(map(tuple, successor_state)) in closed_list:
                continue

            heappush(open_list, successor_node)

    return None


# Example usage:
start_state = [
    [1, 2, 3],
    [8, 7, 6],
    [0, 5, 4]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = astar_search(start_state, goal_state)
if solution:
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")































#
#
#
# explain me this line by line first of all tell me what is this then explain me and prepare 20-30 questions and answers for the same
# ChatGPT
# This is a Python implementation of the A* search algorithm for solving the 8-puzzle problem. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one empty space. The goal is to rearrange the tiles from a given initial state to a goal state by sliding them into the empty space.
#
# Now let's go through the code line by line:
#
# from heapq import heappop, heappush: This line imports the heappop and heappush functions from the heapq module. These functions are used to implement the priority queue, which is an essential component of the A* search algorithm.
#
# class Node:: This line defines a class named Node that represents a node in the search tree. Each node contains the state, the cost to reach that state (g_cost), the estimated cost from that state to the goal state (h_cost), the total cost (f_cost = g_cost + h_cost), and a reference to its parent node.
#
# def __init__(self, state, g_cost, h_cost, parent=None):: This is the constructor method for the Node class. It initializes the node with the provided state, g_cost, h_cost, and an optional parent node.
#
# def __lt__(self, other):: This method overrides the less than (<) comparison operator for nodes. It compares nodes based on their f_cost values, which enables the priority queue to prioritize nodes with lower f_cost.
#
# def heuristic(state, goal_state):: This function calculates the heuristic value for a given state based on the Manhattan distance. The Manhattan distance is the sum of the horizontal and vertical distances between each tile's current position and its goal position.
#
# def get_blank_position(state):: This function finds the position of the blank space (represented by 0) in the given state.
#
# def get_successor_states(state):: This function generates and returns a list of successor states for the given state. Successor states are generated by moving the blank space (0) in different directions (left, right, up, down) within the puzzle grid.
#
# def astar_search(start_state, goal_state):: This is the main A* search function. It takes the start_state and the goal_state as input and returns the path from the start state to the goal state if a solution is found, or None otherwise.
#
# open_list = []: This initializes an empty list to serve as the open list, which contains the nodes that are yet to be explored.
#
# closed_list = set(): This initializes an empty set to serve as the closed list, which contains the states that have been visited and explored.
#
# initial_node = Node(start_state, 0, heuristic(start_state, goal_state), None): This creates the initial node using the start state, with a g_cost of 0, the heuristic value calculated using the heuristic function, and no parent node.
#
# heappush(open_list, initial_node): This adds the initial node to the open list using the heappush function, which maintains the list in a priority queue order based on the nodes' f_cost values.
#
# while open_list:: This starts a loop that continues until the open list is empty, indicating that all possible states have been explored.
#
# current_node = heappop(open_list): This retrieves the node with the lowest f_cost from the open list using the heappop function. Since the open list is a priority queue, the node with the lowest f_cost is always selected.
#
# current_state = current_node.state: This extracts the state from the current node.
#
# if current_state == goal_state:: This checks if the current state is equal to the goal state. If they match, it means the goal state has been reached, and the algorithm proceeds to reconstruct and return the path.
#
# path = []: This initializes an empty list to store the path.
#
# while current_node:: This starts a loop that iterates from the current node to its parent nodes until reaching the start node. It traces back the path from the goal state to the start state.
#
# path.append(current_node.state): This appends the current state to the path list.
#
# current_node = current_node.parent: This updates the current node to its parent node, moving backward in the search tree.
#
# closed_list.add(tuple(map(tuple, current_state))): This adds the current state (converted to a tuple of tuples) to the closed list to mark it as visited.
#
# successors = get_successor_states(current_state): This generates the successor states for the current state using the get_successor_states function.
#
# for successor_state in successors:: This iterates over each successor state.
#
# g_cost = current_node.g_cost + 1: This calculates the g_cost for the successor node by incrementing the g_cost of the current node by 1, as each step has a uniform cost of 1.
#
# h_cost = heuristic(successor_state, goal_state): This calculates the heuristic value for the successor state using the heuristic function.
#
# successor_node = Node(successor_state, g_cost, h_cost, current_node): This creates a new node for the successor state, setting its state, g_cost, h_cost, and parent accordingly.
#
# if tuple(map(tuple, successor_state)) in closed_list:: This checks if the successor state (converted to a tuple of tuples) is already in the closed list. If it is, the state has already been visited, and the loop proceeds to the next successor state.
#
# heappush(open_list, successor_node): This adds the successor node to the open list using the heappush function.
#
# return None: This returns None if no solution is found (i.e., the open list becomes empty without reaching the goal state).
#
# 85-89. The code outside the functions demonstrates an example usage of the A* search algorithm to solve the 8-puzzle problem. It defines a start state and a goal state, then calls the astar_search function with these states. If a solution is found, it prints each state in the solution path. Otherwise, it prints "No solution found."
#
#
# ve the answers too
# ChatGPT
# Certainly! Here are the answers to the questions:
#
# What problem does this code aim to solve?
#
# This code aims to solve the 8-puzzle problem, which involves rearranging numbered tiles on a 3x3 grid to reach a goal state from a given initial state.
# What data structure is used to implement the open list?
#
# The open list is implemented as a priority queue using the heapq module.
# What is the heuristic function used in this implementation?
#
# The heuristic function used in this implementation is the Manhattan distance heuristic.
# How is the Manhattan distance calculated in the heuristic function?
#
# The Manhattan distance is calculated by summing the absolute differences between the current position and the goal position of each tile, both horizontally and vertically.
# How are successor states generated in the get_successor_states function?
#
# Successor states are generated by moving the blank space (represented by 0) in different directions (left, right, up, down) within the puzzle grid.
# How is the priority queue implemented in this code?
#
# The priority queue is implemented using a list, and the heappop and heappush functions from the heapq module to maintain the list in a priority order based on the nodes' f_cost values.
# What information does each node in the search tree store?
#
# Each node in the search tree stores the state, the cost to reach that state (g_cost), the estimated cost from that state to the goal state (h_cost), the total cost (f_cost = g_cost + h_cost), and a reference to its parent node.
# How does the A* search algorithm ensure optimality?
#
# The A* search algorithm ensures optimality by using the sum of the g_cost (the cost to reach the current node) and the heuristic h_cost (the estimated cost from the current node to the goal state) as the evaluation function. This ensures that the algorithm explores the most promising paths first, leading to the optimal solution.
# What is the purpose of the closed list in the A* search algorithm?
#
# The purpose of the closed list is to keep track of the states that have already been visited and explored. It prevents revisiting states and getting caught in cycles, ensuring the algorithm's correctness and efficiency.
# How is the current node selected from the open list in each iteration?
#
# The current node is selected from the open list by using the heappop function, which retrieves the node with the lowest f_cost. Since the open list is implemented as a priority queue, the node with the lowest f_cost is always selected first.
# How is the path from the start state to the goal state reconstructed?
#
# The path from the start state to the goal state is reconstructed by starting from the goal state and tracing back through the parent nodes until reaching the start state. The states are stored in a list, and the list is reversed to get the correct order of states from start to goal.
# What is the time complexity of the A* search algorithm in the worst case?
#
# In the worst case, the time complexity of the A* search algorithm is exponential, specifically O(b^d), where b is the branching factor (average number of successors per state) and d is the depth of the optimal solution.
# What is the space complexity of the A* search algorithm in the worst case?
#
# In the worst case, the space complexity of the A* search algorithm is also exponential, O(b^d), as it needs to store all generated states and nodes in memory.
# What happens if there is no solution to the 8-puzzle problem?
#
# If there is no solution to the 8-puzzle problem, the A* search algorithm will exhaust all possibilities and eventually terminate without finding a path from the start state to the goal state. The function astar_search will return None, indicating that no solution was found.
# Can the heuristic function used in this implementation overestimate the actual cost?
#
# No, the Manhattan distance heuristic used in this implementation does not overestimate the actual cost. It is an admissible heuristic, meaning it never overestimates the actual cost to reach the goal state.
# How does the heappop function select the node with the lowest f_cost from the open list?
#
# The heappop function selects the node with the lowest f_cost from the open list by comparing the f_cost values of the nodes. The nodes are ordered in the priority queue based on their f_cost, and heappop retrieves the node with the lowest value.
# What is the role of the parent attribute in each node?
#
# The parent attribute in each node stores a reference to the parent node in the search tree. It is used to reconstruct the path from the goal state back to the start state once the goal state is reached.
# Why is it important to convert the state to a tuple of tuples before adding it to the closed list?
#
# Converting the state to a tuple of tuples before adding it to the closed list ensures that it is hashable. Lists are mutable and cannot be used as keys in sets or dictionaries, which are commonly used to implement the closed list. By converting the state to a tuple of tuples, it becomes an immutable object that can be used as a key in data structures like sets or dictionaries.
# Can the A* search algorithm be applied to solve problems other than the 8-puzzle?
#
# Yes, the A* search algorithm can be applied to solve a wide range of problems, as long as the problem can be represented as a graph or a search space. It requires defining appropriate state representation, successor generation, and a suitable heuristic function for the specific problem.
# How does the A* algorithm handle tie-breaking when two nodes have the same f_cost?
#
# The A* algorithm handles tie-breaking when two nodes have the same f_cost by using the __lt__ method defined in the Node class. If two nodes have the same f_cost, the __lt__ method compares their f_cost values, and the node with the lower f_cost is considered to have a higher priority.
# Is the A* search algorithm guaranteed to find the optimal solution for any problem?
#
# Yes, the A* search algorithm is guaranteed to find the optimal solution for any problem as long as the heuristic used is admissible (never overestimates the actual cost) and the search space is finite.
# How does the __lt__ method in the Node class affect the behavior of the priority queue?
#
# The __lt__ method in the Node class defines the less-than comparison between two nodes. It determines the order in which nodes are considered in the priority queue. In this case, it compares the f_cost values of nodes, so the node with the lower f_cost is considered smaller and has a higher priority in the queue.
# Is the A* search algorithm guaranteed to terminate?
#
# The A* search algorithm is guaranteed to terminate if a solution exists. However, if there is no solution, the algorithm may continue indefinitely, exploring all possible states until the search space is exhausted.
# How could the heuristic function be modified to improve the efficiency of the search?
#
# The heuristic function could be modified to improve the efficiency of the search by designing a more informed heuristic that provides better estimates of the remaining cost to reach the goal state. A more accurate heuristic can guide the search more effectively and reduce the number of unnecessary explorations.
# Are there any limitations or assumptions in this implementation of the A* search algorithm?
#
# One limitation of this implementation is that it uses the Manhattan distance heuristic, which may not be the most efficient heuristic for all instances of the 8-puzzle. Additionally, this implementation assumes that the start state and goal state are valid and reachable configurations of the puzzle.
# What modifications would be necessary to apply this algorithm to a larger puzzle grid?
#
# To apply this algorithm to a larger puzzle grid, modifications would be needed in the code to handle the increased size of the grid and adjust the successor generation, heuristic function, and state representation accordingly.
# Can the A* search algorithm handle problems with varying costs for different actions?
#
# Yes, the A* search algorithm can handle problems with varying costs for different actions. The g_cost in the Node class can be modified to account for different costs associated with each action. By adjusting the g_cost accordingly, the algorithm can consider different action costs during the search.
# How does the A* search algorithm compare to other search algorithms like breadth-first search or depth-first search?
#
# The A* search algorithm is generally more informed and efficient compared to breadth-first search and depth-first search. A* uses heuristics to guide the search towards the goal, while breadth-first search explores all possible states at a given depth before moving deeper, and depth-first search explores a path as far as possible before backtracking.
# Are there any potential optimizations that could be implemented to improve the performance of the A* search algorithm?
#
# Yes, there are several potential optimizations to improve the performance of the A* search algorithm. These include techniques like memoization, pruning redundant states, using better heuristics, and implementing techniques like IDA* (Iterative Deepening A*) or SMA* (Simplified Memory-Bounded A*) to limit memory usage.
# How does the choice of heuristic function affect the performance and optimality of the A* search algorithm?
#
# The choice of heuristic function can significantly affect the performance and optimality of the A* search algorithm. An admissible heuristic provides a lower bound on the actual cost and guarantees the optimality of the solution. However, an informed heuristic that provides a tighter estimate can improve the algorithm's efficiency by reducing the number of explored states.
#
#

