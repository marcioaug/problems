from queue import PriorityQueue


def prim(graph):

    MST = set()
    X = set()

    vertices = len(graph[0])

    X.add(0)

    while len(X) != vertices:
        crossing = set()

        for x in X:
            for k in range(vertices):

                if k not in X and graph[x][k] != 0:
                    crossing.add((x, k))

        edge = sorted(crossing, key=lambda e: graph[e[0]][e[1]])[0]

        MST.add(edge)
        X.add(edge[1])

    return MST


def prim_2(graph):

    MST = set()
    X = set()

    vertices = len(graph[0])

    X.add(0)

    while len(X) != vertices:
        crossing = PriorityQueue()

        for x in X:
            for k in range(vertices):
                if k not in X and graph[x][k] != 0:
                    crossing.put([graph[x][k], (x, k)])

        edge = crossing.get()

        MST.add(edge[1])
        X.add(edge[1][1])

    return MST


def prim_3(graph):
    queue = PriorityQueue()
    queue.put([0, start])

    while not queue.empty():
        node = queue.get()

        # if node[0] <= dist[node[1]]:
        for vertex in graph[node[1]]:
            if dist[vertex[0]] == None or dist[vertex[0]] > node[0] + vertex[1]:
                dist[vertex[0]] = node[0] + vertex[1]
                queue.put([dist[vertex[0]], vertex[0]])

    return dist


if __name__ == '__main__':

    graph = [
        [0, 2, 1],
        [2, 0, 0],
        [1, 0, 0],
    ]

    A = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    print(prim(graph))
    print(prim_2(graph))
    print(prim_2(A))

    # 0, 5, 2, 3, 6, 7, 0, 2
    # 0, 2, 7, 0, 2, 3, 5, 6