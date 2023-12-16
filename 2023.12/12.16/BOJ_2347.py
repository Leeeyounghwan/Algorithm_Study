import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

balloons = deque(enumerate(map(int, input().split())))
li = []

while balloons:
    idx, cnt = balloons.popleft()
    li.append(idx + 1)

    if cnt > 0:
        balloons.rotate(-(cnt - 1))
    elif cnt < 0:
        balloons.rotate(-(cnt))

print(" ".join(map(str, li)))
