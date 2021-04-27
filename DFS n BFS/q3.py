from sys import stdin
from collections import deque

def getComplex():
    cnt = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                matrix[r][c] = 0
                cnt.append(1)
                dfs(r, c, cnt)
    return cnt

def dfs(r, c, cnt):
    check_r = [0, -1, 0, 1]
    check_c = [-1, 0, 1, 0]
    for idx in range(4):
        temp_r = check_r[idx] + r
        temp_c = check_c[idx] + c
        if temp_r < 0 or temp_c < 0 or temp_r >= N or temp_c >= N:
            continue
        if matrix[temp_r][temp_c] == 1:
            matrix[temp_r][temp_c] = 0
            cnt[-1] += 1
            dfs(temp_r, temp_c, cnt)

if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    matrix = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
    res = getComplex()
    print(len(res))
    print("\n".join(map(str, sorted(res))))



