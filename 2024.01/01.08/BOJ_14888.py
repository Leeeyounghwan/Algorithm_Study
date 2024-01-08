import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))        # +, -, *, /의 갯수

max_val = -1e9
min_val = 1e9

def dfs(depth, sum, add, sub, mul, div):
    global max_val, min_val
    if depth == N:
        max_val = max(sum, max_val)
        min_val = min(sum, min_val)
        return
    
    if add:
        dfs(depth + 1, sum + numbers[depth], add - 1, sub, mul, div)
    if sub:
        dfs(depth + 1, sum - numbers[depth], add, sub - 1, mul, div)
    if mul:
        dfs(depth + 1, sum * numbers[depth], add, sub, mul - 1, div)
    if div:
        dfs(depth + 1, int(sum / numbers[depth]), add, sub, mul, div - 1)

dfs(1, numbers[0], op[0], op[1], op[2], op[3])
print(max_val)
print(min_val)
    