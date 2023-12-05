import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
cnt = []

# 체스판 입력받기
for _ in range(N):
    board.append(input().rstrip())

for i in range(N - 7):
    for j in range(M - 7):
        cnt_W = 0  # W로 시작할 경우 바뀐 체스판의 갯수
        cnt_B = 0  # B로 시작할 경우 바뀐 체스판의 갯수
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != "W":
                        cnt_W += 1
                    if board[k][l] != "B":
                        cnt_B += 1
                else:
                    if board[k][l] != "B":
                        cnt_W += 1
                    if board[k][l] != "W":
                        cnt_B += 1
        cnt.append(min(cnt_W, cnt_B))

print(min(cnt))
