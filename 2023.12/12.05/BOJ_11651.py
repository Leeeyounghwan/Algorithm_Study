import sys

input = sys.stdin.readline

N = int(input())

li = []

for _ in range(N):
    x, y = map(int, input().split())
    li.append([y, x])

li.sort()

for item in li:
    print(item[1], item[0])
