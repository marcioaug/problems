#! /usr/bin/python3
from queue import PriorityQueue

def prim(G):

    MST = {}
    MST_edges = set()
    cost = 0
    queue = PriorityQueue()
    visited = []

    r = list(G.keys())[0]
    
    V = G[r]
    visited.append(r)

    for v in V:
        queue.put((v[1], v[0], r))

    while not queue.empty():
        e = queue.get()
        if e[1] not in visited:
            visited.append(e[1])
            for v in G[e[1]]:
                if v[0] not in visited:
                    queue.put((v[1], v[0], e[1]))
            
            if e[2] not in MST:
                MST[e[2]] = []
            MST[e[2]].append((e[1], e[0]))

            if e[1] not in MST:
                MST[e[1]] = []
            MST[e[1]].append((e[2], e[0]))

            if e[2] <= e[1]:
                MST_edges.add((e[2], e[1], e[0]))
            else:
                MST_edges.add((e[1], e[2], e[0]))

            cost += e[0]

    return MST, MST_edges, cost


def dfs(G, V, cost, costs, visited):
    visited.append(V)
    for v in G[V]:
        if v[0] not in visited:
            c = cost + v[1]
            costs.append((v[0], c))
            dfs(G, v[0], c, costs, visited)
    return costs

def main():
    (v, e, r) = map(int, input().split())

    G = {}

    for _ in range(e):
        (f, t, w) = map(int, input().split())

        if f not in G:
            G[f] = []
        G[f].append((t, w))

        if t not in G:
            G[t] = []
        G[t].append((f, w))

    MST, MST_edges, cost  = prim(G)

    print('########################')
    print('Minimum Cost:')
    print(cost)
    print('########################')
    print('Connections:')
    for edge in sorted(MST_edges):
        print(str(edge[0]) + " " + str(edge[1]))
    print('########################')
    print('Pings:')
    for cost in sorted(dfs(MST, 0, 0, [], [])):
        print('%d: %.3f' % (cost[0], (2 * cost[1]) / r))
    print('########################')

if __name__ == '__main__':
    main()
