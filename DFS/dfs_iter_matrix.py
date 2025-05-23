def dfs_iter_matrix(graph, start, total):
    visited = [False] * total
    stack = []
    order = []

    stack.append(start)

    while stack:
        current_node = stack.pop()
        if visited[current_node] == False:
            visited[current_node] = True #visit as we pop off the stack
            order.append(current_node)
            neighbor = 0
            while neighbor < total:
                if graph[current_node][neighbor] == 1 and visited[neighbor] == False
                    stack.append(neighbor)
                neighbor += 1


