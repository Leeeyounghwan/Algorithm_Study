import sys

input = sys.stdin.readline

N = int(input())

li = []

for _ in range(N):
    x, y = map(int, input().split())
    li.append([x, y])
li.sort()

for item in li:
    print(item[0], item[1])
