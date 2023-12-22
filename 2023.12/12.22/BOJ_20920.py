import sys

input = sys.stdin.readline

N, M = map(int, input().split())

words = {}

for i in range(N):
    word = input().rstrip()
    
    if len(word) < M:
        continue
    else:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1


memory = sorted(words, key = lambda x: (-words[x], -len(x), x))

for word in memory:
    print(word)