import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())

li = [i for i in range(1, N+1)]

per = list(product(li, repeat = M))
per.sort()

for item in per:
    print(" ".join(map(str, item)))