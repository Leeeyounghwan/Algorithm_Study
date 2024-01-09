import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]

cnt = 0

for i in reversed(range(N)):
    cnt += K // coin[i]
    K = K % coin[i]

print(cnt)