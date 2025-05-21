
#visit as we queue up a node
def bfs_matrix(graph, start_node, total_nodes):
    visited = [False] * total_nodes
    queue = []
    order = []

    #Queue up the start node
    queue.append(start_node)
    visited[start_node] = True
    order.append(start_node)


    #begin process
    while queue:
        current = queue.pop(0) #get first item in queue
        #visited[current] = True
        #order.append(current) #visit it
        neighbor = 0

        #queue up all of current nodes direct neighbors to be visited later
        while neighbor < total_nodes:
            if graph[current][neighbor] == 1 and visited[neighbor] == False:
                queue.append(neighbor)
                visited[neighbor] = True #visit it
                order.append(neighbor)
            neighbor += 1

    return order






#MAIN CALLING ROUTINE
adjacency_matrix = [
    [0,0,0,0,0,1],
    [0,0,1,1,0,0],
    [0,1,0,1,1,0],
    [0,1,1,0,1,1],
    [0,0,1,1,0,0],
    [1,0,0,1,1,0]
]

order_visited = bfs_matrix(adjacency_matrix, 2, 6)
print(order_visited)
print(f"\nThrough BFS run on an adjacency MATRIX, we visited all the verticies, where the index value of the list represents the vertex: {order_visited}")
