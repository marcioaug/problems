from queue import PriorityQueue


def dijktra(graph, start, dist):

    queue = PriorityQueue()
    queue.put([0, start])

    dist[start] = 0

    while not queue.empty():
        node = queue.get()

        if node[0] <= dist[node[1]]:
            for vertex in graph[node[1]]:
                if dist[vertex[0]] == None or dist[vertex[0]] > node[0] + vertex[1]:
                    dist[vertex[0]] = node[0] + vertex[1]
                    queue.put([dist[vertex[0]], vertex[0]])
    
    return dist


if __name__ == '__main__':

    graph = [
        [[5, 14], [2, 9], [1, 7]],
        [[0, 7], [2, 10], [3, 14]],
        [[0, 9], [1, 10], [5, 2], [3, 11]],
        [[1, 15], [2, 11], [4, 6]],
        [[3, 6], [5, 9]],
        [[0, 14], [2, 2], [4, 9]]
    ]

    dist = [None for index in graph]

    print(dijktra(graph, 0, dist))