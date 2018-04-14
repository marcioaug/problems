#! /usr/bin/python3
from math import ceil, log2

def build(A, tree):

    for i in range(len(A)):
        tree[len(A) + i] = A[i]

    for i in reversed(range(len(A) - 1)):
        tree[i >> 1] = max(tree[i], tree[i^1])

def main():
    n = int(input())
    sections = []

    for _ in range(n):
        sections.append(int(input()))

    tree = [1 for _ in range(2 * len(sections))]
    build(sections, tree)

    print(tree)


if __name__ == '__main__':
    main()