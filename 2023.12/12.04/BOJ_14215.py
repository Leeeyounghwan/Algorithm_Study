import sys

input = sys.stdin.readline

li = sorted(list(map(int, input().split())))

if (li[0] + li[1]) > li[2]:
    print(sum(li))
else:
    print((li[0] + li[1]) * 2 - 1)
