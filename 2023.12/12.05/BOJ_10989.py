import sys

input = sys.stdin.readline

N = int(input())

li = [0] * 10001

for _ in range(N) :
    li[int(input())] += 1

for i in range(len(li)):
    if li[i] != 0:
        for _ in range(li[i]):
            print(i)