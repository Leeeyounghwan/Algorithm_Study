import sys

input = sys.stdin.readline

N, M = map(int, input().split())

hear = set()
see = set()

for _ in range(N):
    name = input().rstrip()
    hear.add(name)

for _ in range(M):
    name = input().rstrip()
    see.add(name)

answer = sorted(list(hear & see))

print(len(answer))
for item in answer:
    print(item)
