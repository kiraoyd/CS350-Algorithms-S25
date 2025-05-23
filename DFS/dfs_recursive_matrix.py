def dfs_wrapper_matrix(matrix, start, total):
    visited = [False] * total
    order = []
    dfs_recursive_matrix(matrix, start, total, visited, order)
    print(order)

def dfs_recursive_matrix(graph, current, total, visited, order):
    if current >= total or visited[current] == True:
        return
    visited[current] = True
    order.append(current)

    neighbor = 0
    while neighbor < total:
        if graph[current][neighbor] == 1 and visited[neighbor] == False:
            dfs_recursive_matrix(graph, neighbor, total, visited, order)
        neighbor += 1


#---MAIN CALLING ROUTINE---#

matrix = [
    [0,0,0,0,0,0,0,0,0,0,1],
    [0,0,1,0,0,1,0,1,0,0,0],
    [0,1,0,1,0,1,1,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,1,1,0],
    [0,1,1,0,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0]
]

start = 5
total_nodes = 11
dfs_wrapper_matrix(matrix, start, total_nodes)