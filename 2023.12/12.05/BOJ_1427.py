import sys

input = sys.stdin.readline

N = int(input())

li = []
for i in str(N):
    li.append(int(i))

li.sort(reverse=True)

for item in li:
    print(item, end="")
