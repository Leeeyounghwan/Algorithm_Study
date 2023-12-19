import sys

""" combinations 사용해서 풀어보기 """
# from itertools import combinations

# input = sys.stdin.readline

# N, K = map(int, input().split())

# li = [i for i in range(N)]

# print(len(list(combinations(li, K))))

""" 재귀함수로 풀어보기 """
input = sys.stdin.readline

N,K = map(int, input().split())

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

answer = factorial(N) // (factorial(K) * factorial(N - K))
print(answer)