from sys import stdin
from collections import deque

def bfs(arr):
    res = 1
    pos = [[-1, 0],[1, 0],[0, -1],[0, 1]] # 상 하 좌 우
    visited = [[[False] * m for _ in range(n)] for i in range(2)]
    queue = deque([[0, 0, 0]])
    arr[0][0] = -1
    size = 1
    while queue:
        t = queue.popleft()
        for p in pos:
            temp_r = t[0] + p[0]
            temp_c = t[1] + p[1]
            if temp_r < 0 or temp_c < 0 or temp_r >= n or temp_c >= m:
                continue

            if visited[t[2]][temp_r][temp_c]:
                continue

            if temp_r == n-1 and temp_c == m-1:
                return res + 1

            if arr[temp_r][temp_c] == '0':
                visited[t[2]][temp_r][temp_c] = True
                queue.append([temp_r, temp_c, t[2]])

            elif arr[temp_r][temp_c] == '1' and t[2] == 0:
                visited[1][temp_r][temp_c] = True
                queue.append([temp_r, temp_c, 1])

        size -= 1
        if size == 0:
            res += 1
            size = len(queue)
    return -1


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    board = [list(stdin.readline().rstrip()) for _ in range(n)]
    print(bfs(board) if len(board) != 1 else 1)