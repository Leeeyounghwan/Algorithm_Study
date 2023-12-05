import sys

input = sys.stdin.readline

li = []

for _ in range(5):
    li.append(int(input()))
li.sort()

print(int(sum(li) // 5))
print(li[2])
