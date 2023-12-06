import sys

input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    li.append(input().rstrip())

li = list(set(li))

li.sort()
li.sort(key=len)

for item in li:
    print(item)
