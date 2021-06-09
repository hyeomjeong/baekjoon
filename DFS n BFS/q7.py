from sys import stdin
from collections import deque

def bfs(board_size, curr):
    res = 0
    pos = [[-1, -2],[-2, -1],[-2, 1],[-1, 2],[1, 2],[2, 1],[2, -1],[1, -2]] # 좌상 우상 우하 좌하 좌상부터 시계방향
    board = [[False]*board_size for _ in range(board_size)]
    queue = deque([curr])
    size = len(queue)
    while queue:
        r, c = queue.popleft()
        for p in pos:
            temp_r = r + p[0]
            temp_c = c + p[1]

            if temp_r < 0 or temp_c < 0 or temp_r >= board_size or temp_c >= board_size:
                continue

            if [temp_r, temp_c] == target_pos:
                return res + 1

            if not board[temp_r][temp_c]:
                board[temp_r][temp_c] = True
                queue.append([temp_r, temp_c])

        size -= 1
        if size == 0:
            size = len(queue)
            res += 1

    return -1

if __name__ == '__main__':
    tc = int(stdin.readline().rstrip())
    for _ in range(tc):
        m = int(stdin.readline().rstrip())
        curr_pos = list(map(int, stdin.readline().split()))
        target_pos = list(map(int, stdin.readline().split()))
        print(bfs(m, curr_pos) if curr_pos != target_pos else 0)