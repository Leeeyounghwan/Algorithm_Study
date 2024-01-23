import sys

input = sys.stdin.readline

numbers = set(range(1, 10000))
remove = set()

for i in numbers:
    for j in str(i):
        i += int(j)
    remove.add(i)

self = numbers - remove
for item in sorted(self):
    print(item)