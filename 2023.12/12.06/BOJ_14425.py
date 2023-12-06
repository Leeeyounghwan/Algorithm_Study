import sys

input = sys.stdin.readline

N, M = map(int, input().split())

word_dict = {}
cnt = 0

for i in range(N):
    word_dict[input().rstrip()] = 0

for _ in range(M):
    if input().rstrip() in word_dict:
        cnt += 1

print(cnt)
