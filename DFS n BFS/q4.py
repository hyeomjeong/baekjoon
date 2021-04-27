from sys import stdin
from collections import deque

def bfs(n, k):
    visited = [False for _ in range(100001)]
    visited[n] = True

    queue = deque([[n, 0]])
    while len(queue) > 0:
        x = queue.popleft()
        step = [-1, 1, x[0]]
        for idx in range(3):
            t = x[0] + step[idx]
            if t < 0 or t > 100000 or visited[t]:
                continue
            if t == k:
                return x[1] + 1
            visited[t] = True
            queue.append([t, x[1]+1])

    return -1



if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    if N == K:
        print(0)
    else:
        print(bfs(N, K))