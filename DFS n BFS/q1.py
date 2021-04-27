from sys import stdin
from collections import deque

def dfs(res, v_list, i):
    v_list[i] = True
    res.append(i + 1)

    for j in range(N):
        if matrix[i][j] == 1 and not v_list[j]:
            dfs(res, v_list, j)


def bfs(res, v):
    v_list = [False for _ in range(N)]

    res.append(v+1)
    v_list[v] = True
    queue = deque([v])

    while len(queue) > 0:
        t = queue.popleft()
        for idx in range(N):
            if not v_list[idx] and matrix[t][idx] == 1:
                v_list[idx] = True
                queue.append(idx)
                res.append(idx + 1)


if __name__ == '__main__':
    N, M, V = map(int, stdin.readline().split())
    matrix = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        matrix[a-1][b-1] = matrix[b-1][a-1] = 1

    dfs_result = []
    dfs(dfs_result, [False for _ in range(N)], V-1)

    bfs_result = []
    bfs(bfs_result, V-1)

    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))

