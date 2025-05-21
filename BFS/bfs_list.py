
def bfs_list(graph, start_node, total_nodes):
    visited = [False] * total_nodes
    queue = []
    order = []

    #queue up the start node
    queue.append(start_node)
    visited[start_node] = True
    order.append(start_node)

    #begin process
    while queue:
        current = queue.pop(0) #get first item in queue

        neighbors = graph[current] #get list of currents neighbors

        #traverse the list of neighbors
        index = 0
        while index < len(neighbors):
            neighbor = neighbors[index] #get a neighbor
            if visited[neighbor] == False:
                queue.append(neighbor) #queue up the neighbor
                visited[neighbor] = True #visit it
                order.append(neighbor)


            index += 1

    return order



adjacency = {
    0: [5],
    1: [2,3],
    2: [1,3,4],
    3: [1,2,4,5],
    4: [2,3,5],
    5: [0,3,4]
}

number = 6
order_visited_list = bfs_list(adjacency, 2, number)
print(f"\nThrough BFS run on an adjacency LIST, we visited all the verticies, where the index value of the list represents the vertex: {order_visited_list}")