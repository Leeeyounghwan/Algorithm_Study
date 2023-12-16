import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    command = input().rstrip()
    if len(command) > 1:
        command = list(map(int, command.split()))
        if command[0] == 1:
            queue.appendleft(int(command[1]))
        else:
            queue.append(int(command[1]))

    elif command[0] == "3":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)

    elif command[0] == "4":
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)

    elif command[0] == "5":
        print(len(queue))

    elif command[0] == "6":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "7":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)

    elif command[0] == "8":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
