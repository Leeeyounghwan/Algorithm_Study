import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)

dic = {}

for i in range(0, 10):
    dic[i] = 0

for c in map(str, mul):
    char = int(c)
    if char in dic:
        dic[char] += 1

for i in dic:
    print(dic[i])