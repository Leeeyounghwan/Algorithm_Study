import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])
ysps = []


while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    ysps.append(queue.popleft())

print("<", end="")
print(", ".join(map(str, ysps)), end="")
print(">")
