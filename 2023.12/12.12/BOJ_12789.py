import sys

input = sys.stdin.readline

N = int(input())

wait = list(map(int, input().split()))

stack = []
target = 1

while wait:
    if wait[0] == target:
        wait.pop(0)
        target += 1
    else:
        stack.append(wait.pop(0))
    
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break

if len(stack) == 0:
    print("Nice")
    
else:
    print("Sad")
