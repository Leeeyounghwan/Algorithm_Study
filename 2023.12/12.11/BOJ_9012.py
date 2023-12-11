import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    vps = input().rstrip()

    stack = []

    for s in vps:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break

    else:
        if not stack:
            print("YES")
        else:
            print("NO")
