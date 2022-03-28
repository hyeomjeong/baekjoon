from sys import stdin
from collections import deque

def bfs(x):
    queue = deque([x])
    colors[x] = 1

    while queue:
        curr_idx = queue.popleft()
        for adj in graph[curr_idx]:
            if colors[adj] == 0:
                colors[adj] = -colors[curr_idx]
                queue.append(adj)
            elif colors[curr_idx] + colors[adj] != 0:
                return False
    return True

if __name__ == '__main__':
    k = int(stdin.readline().rstrip())
    for _ in range(k):
        v, e = map(int, stdin.readline().split())
        graph = [[] * v for _ in range(v)]
        for _ in range(e):
            a, b = map(int, stdin.readline().split())
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        res = True
        colors = [0] * v
        for idx in range(v):
            if colors[idx] == 0:
                if not bfs(idx):
                    res = False
                    break

        print("YES" if res else "NO")

