import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    command = input().rstrip()

    # push
    if len(command) > 2:
        com, num = map(int, command.split())
        stack.append(num)
    
    # pop
    if command == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    # length
    if command == '3':
        print(len(stack))

    # isempty
    if command == '4':
        if len(stack) == 0:
            print(1)
        else: print(0)
    
    # top
    if command == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])