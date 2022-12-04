# Calculating the shortest distance between two points on a graph or map

# Import the priority queue library
from queue import PriorityQueue

# Define a function to calculate the shortest distance between two points in a graph or map
def dijkstra(graph, start, end):
    # We create a priority queue to store the nodes to visit.
    queue = PriorityQueue()
    # Add the starting node to the priority queue, with an initial distance of 0
    queue.put((0, start))
    # Create a dictionary to store visited nodes and their shortest distances
    visited = {}
    # We initialise the dictionary of visited nodes with the shortest distance of the starting node as 0
    visited[start] = 0

    # As long as the queue with priority is not empty
    while not queue.empty():
        # We get the current node and its shortest distance from the starting node.
        current_distance, current_node = queue.get()
        # If the current node is the end node, we return its shortest distance from the initial node
        if current_node == end:
            return current_distance
        # If the current node is not in the dictionary of visited nodes, we continue with the next node
        if current_node not in visited:
            continue

        # Traverse all nodes adjacent to the current node
        for neighbour, distance in graph[current_node].items():
            # We calculate the shortest distance to the neighbour node by adding the distance from the current node.
            new_distance = current_distance + distance
            # If the shortest distance to the neighbouring node is less than the distance stored in the dictionary
            # of visited nodes, we update the distance in the dictionary and add the neighbouring node to the queue
            # with priority
            if neighbour not in visited or new_distance < visited[neighbour]:
                visited[neighbour] = new_distance
                queue.put((new_distance, neighbour))

    # If we got this far, it's because no path was found from the start node to the end node.
    return -1

# We create a dictionary representing the graph or map with the distances between each pair of nodes
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

# We ask the user to enter the start node and the end node.
start = input("Enter the start node: ")
end = input("Enter the end node: ")

# We calculate the shortest distance between the start node and the end node using Dijkstra's algorithm
shortest_distance = dijkstra(graph, start, end)

# Print the shortest distance between the start node and the end node
print("The shortest distance between the start node and the end node is:", shortest_distance)