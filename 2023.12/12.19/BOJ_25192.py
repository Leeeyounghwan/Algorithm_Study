import sys

input = sys.stdin.readline

N = int(input())

cnt = 0

member = set()

for _ in range(N):
    command = input().rstrip()

    if command == "ENTER":
        cnt += len(member)
        member.clear()
    else:
        member.add(command)

cnt += len(member)
print(cnt)