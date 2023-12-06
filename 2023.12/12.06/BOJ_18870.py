import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
li = list(set(numbers))
li.sort()

num_dict = {}

for i in range(len(li)):
    dict[li[i]] = i

for i in numbers:
    print(num_dict[i], end=" ")
