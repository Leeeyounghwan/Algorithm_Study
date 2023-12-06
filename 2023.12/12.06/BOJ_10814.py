import sys

input = sys.stdin.readline

N = int(input())

li = []

for _ in range(N):
    age, name = input().split()
    li.append([int(age), name])
li.sort(key=lambda x: x[0])

for item in li:
    print(item[0], item[1])
