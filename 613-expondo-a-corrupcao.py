#! /usr/bin/python3


def backpack(value_1, value_2, weight, i, capacity, store={}):

    if i in store:
        if capacity in store[i]:
            return store[i][capacity]
    else:
        store[i] = {}

    result = 0

    if i != len(weight) and capacity != 0:
        if weight[i] > capacity:
            return value_1[i] + backpack(value_1, value_2, weight, i + 1, capacity, store)
        else:   
            result =  max(
                value_2[i] + backpack(value_1, value_2, weight, i + 1, capacity - weight[i], store),
                value_1[i] + backpack(value_1, value_2, weight, i + 1, capacity, store)
            )
    
    store[i][capacity] = result
    return result


def dfs(graph, edge, visited, costs):
    cost = costs[edge] if not visited[edge] else 0
    members = [edge] if not visited[edge] else None
 
    visited[edge] = True

    for child in graph[edge]:
        if not visited[child]:
            c, m = dfs(graph, child, visited, costs)
            cost += c
            members += m

    return cost, members


def flood_fill(politicians, costs, dp_size):
    itens = []
    visited = [False for _ in politicians]

    for i in range(len(politicians)):
        cost, group = dfs(politicians, i, visited, costs)
        if group:
            itens.append((cost, group, [i for i in group if i < dp_size], [i for i in group if i >= dp_size]))

    return itens


def main():
    D, P, R, B = map(int, input().split())

    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    politicians = [[] for _ in range(len(S) + len(T))]
    costs = S + T

    for _ in range(R):
        s, t = map(int, input().split())
        politicians[s - 1].append(len(S) + t - 1)
        politicians[len(S) + t - 1].append(s - 1)

    itens = flood_fill(politicians, costs, len(S))
    
    value_dp = [len(i[2]) for i in itens]
    value_prism = [len(i[3]) for i in itens]
    weight = [i[0] for i in itens]

    print(
        backpack(value_dp, value_prism, weight, 0, B, {}), 
        backpack(value_prism, value_dp, weight, 0, B, {})
    )


if __name__ == '__main__':
    main()
