import sys

input = sys.stdin.readline

def dac(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (dac(A, B // 2, C) ** 2) % C
    else:
        return ((dac(A, B // 2, C) ** 2) * A) % C

A, B, C = map(int, input().split())


print(dac(A, B, C)) 