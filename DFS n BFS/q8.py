from sys import stdin
from collections import deque

def bfs():
    colors = [0] * v
    queue = deque([0])
    colors[0] = 1

    while queue:
        curr_idx = queue.popleft()
        for adj_idx in range(v):
            if adj_idx in graph[curr_idx]:
                if colors[adj_idx] == 0:
                    colors[adj_idx] = -colors[curr_idx]
                    queue.append(adj_idx)
                elif colors[curr_idx] + colors[adj_idx] != 0:
                    return "NO"
    return "YES"

if __name__ == '__main__':
    k = int(stdin.readline().rstrip())
    for _ in range(k):
        v, e = map(int, stdin.readline().split())
        graph = [[] * v for _ in range(v)]
        for _ in range(e):
            a, b = map(int, stdin.readline().split())
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        print(bfs())

