import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

li = [i for i in range(1, N + 1)]

combi = list(combinations(li, M))
combi.sort()

for item in combi:
    print(" ".join(map(str, item)))
