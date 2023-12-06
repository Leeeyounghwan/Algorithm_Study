import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_dict = {}

for i in range(1, N + 1):
    pokemon = input().rstrip()
    pokemon_dict[pokemon] = i
    pokemon_dict[i] = pokemon

for _ in range(M):
    check = input().rstrip()
    if check.isdigit() == True:
        print(pokemon_dict[int(check)])
    else:
        print(pokemon_dict[check])