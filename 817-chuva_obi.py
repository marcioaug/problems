#! /usr/bin/python3
from math import ceil, log2

def build(A, pos, low, high, tree):

    if low == high:
        tree.insert(pos, A[low])
    else:
        mid = (high + low) // 2

        build(A, 2 * pos, low, mid, tree)
        build(A, 2 * pos + 2, mid + 1, high, tree)

        print(2 * pos + 1)
        print(2 * pos + 2)

        tree.insert(pos, max(tree[2 * pos], tree[2 * pos + 1]))




def main():
    n = int(input())
    sections = []

    for _ in range(n):
        sections.append(int(input()))

    #tree = [0 for _ in range(int(pow(2, int(ceil(log2(len(sections)))))))]
    tree = []
    print(len(tree))
    build(sections, 1, 0,  len(sections) -1, tree)

    print(sections)
    print(tree)


if __name__ == '__main__':
    main()