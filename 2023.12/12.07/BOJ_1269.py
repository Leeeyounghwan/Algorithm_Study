import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A_li = set(map(int, input().split()))
B_li = set(map(int, input().split()))

cnt = 0

cnt += len(A_li - B_li) + len(B_li - A_li)

print(cnt)
