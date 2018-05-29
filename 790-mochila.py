#! /usr/bin/python3


def backpack(value, weight, i, capacity, store={}):

    if i in store:
        if capacity in store[i]:
            return store[i][capacity]
    else:
        store[i] = {}

    result = 0

    if capacity != 0 and i != len(weight):
        if weight[i] > capacity:
            result =  backpack(value, weight, i + 1, capacity, store)
        else:
            result =  max(
                value[i] + backpack(value, weight, i + 1, capacity - weight[i], store),
                backpack(value, weight, i + 1, capacity, store)
            )
    
    store[i][capacity] = result
    return result


def main():
    n, p = map(int, input().split())

    value = list(map(int, input().split()))
    weight = list(map(int, input().split()))

    print("%d" % backpack(value, weight, 0, p))


if __name__ == '__main__':
    main()