import sys

input = sys.stdin.readline

S = input().rstrip()
answer = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        tmp = S[i : j + 1]
        answer.add(tmp)
print(len(answer))
