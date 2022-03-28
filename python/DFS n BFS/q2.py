from sys import stdin
from collections import deque

def bfs(n):
    visited = [False] * computer
    visited[n] = True
    queue = deque([n])
    cnt = 0
    while len(queue) > 0:
        t = queue.popleft()
        for idx in range(computer):
            if not visited[idx] and matrix[t][idx] == 1:
                queue.append(idx)
                visited[idx] = True
                cnt += 1
    return cnt

if __name__ == '__main__':
    computer = int(stdin.readline().rstrip())
    line = int(stdin.readline().rstrip())

    matrix = [[0] * computer for _ in range(computer)]
    for _ in range(line):
        a, b = map(int, stdin.readline().split())
        matrix[a - 1][b - 1] = matrix[b - 1][a - 1] = 1

    print(bfs(0))