def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        edge = queue.pop(0)        
        print(edge)
        for child in graph[edge]:            
            if not visited[child]:             
                queue.append(child)
                visited[child] = True


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

    bfs(graph, 0, visited)

