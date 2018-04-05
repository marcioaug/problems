
def dfs(graph, edge, visited):
    visited[edge] = True

    for child in graph[edge]:
        try:
            if not visited[child]:
                pass
        except:
            dfs(graph, child, visited)

def dfs_2(graph, edge, visited):
    visited[edge] = True
    print(edge)
    for child in graph[edge]:
        if not visited[child]:
            dfs_2(graph, child, visited)


if __name__ == '__main__':

    graph = [
        [1],
        [0, 2, 3],
        [1, 3],
        [1, 2, 4],    
        [3],
        [],
        [7, 8],
        [6],
        [6]
    ]

    visited = [False for index in graph]

    dfs(graph, 0, {})
    dfs_2(graph, 0, visited)