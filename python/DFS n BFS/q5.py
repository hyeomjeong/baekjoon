from sys import stdin
from collections import deque

def bfs(arr):
    pos = [[0,0,-1],[0,-1,0],[0,0,1],[0,1,0],[-1,0,0],[1,0,0]] #왼쪽 위쪽 오른쪽 아래쪽 위 아래
    res = -1
    queue = deque([])

    for h_idx in range(h):
        for r_idx in range(n):
            for c_idx in range(m):
                if arr[h_idx][r_idx][c_idx] == 1:
                        queue.append([h_idx, r_idx, c_idx])
    if check(arr):
        return 0

    q_size = len(queue)
    while queue:
        tmp = queue.popleft()

        for p in pos:
            temp_h = tmp[0] + p[0]
            temp_r = tmp[1] + p[1]
            temp_c = tmp[2] + p[2]
            if temp_h < 0 or temp_r < 0 or temp_c < 0 or temp_h >= h or temp_r >= n or temp_c >= m:
                continue
            if arr[temp_h][temp_r][temp_c] == 0:
                arr[temp_h][temp_r][temp_c] = 1
                queue.append([temp_h, temp_r, temp_c])

        q_size -= 1
        if q_size == 0:
            q_size = len(queue)
            res += 1


    return res if check(arr) else -1


def check(arr):
    for a in arr:
        for t in a:
            if 0 in t:
                return False
    return True


if __name__ == '__main__':
    m, n, h = map(int, stdin.readline().split())
    box = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]
    print(bfs(box))