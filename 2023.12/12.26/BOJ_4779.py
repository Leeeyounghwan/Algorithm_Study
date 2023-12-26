import sys

input = sys.stdin.readline

def cut(n):
    if n == 1:
        return "-"
    left = cut(n // 3)
    center = " " * (n // 3)
    return left + center + left

while True:
    try:
        N = int(input())

        res = cut(3 ** N)
        print(res)
    except:
        break