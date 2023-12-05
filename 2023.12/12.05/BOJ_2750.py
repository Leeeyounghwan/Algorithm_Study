import sys

input = sys.stdin.readline

N = int(input())
li = []

for i in range(N):
    li.append(int(input()))

li.sort()

for item in li:
    print(item)
