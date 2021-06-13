from sys import stdin
# import heapq

if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    adj_list = {x: {} for x in range(1, N+1)}
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        adj_list[A][B] = C if B not in adj_list[A].keys() else min(C, adj_list[A][B])
    flag = False
    distances = [float('inf')] * (N+1)
    distances[1] = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            for a in adj_list[j]:
                d = adj_list[j][a]
                if distances[j] != float('inf') and distances[a] > distances[j] + d:
                    distances[a] = distances[j] + d
                    if i == N:
                        flag = True
    print('\n'.join(map(lambda x: str(x) if x != float('inf') else "-1", distances[2:])) if not flag else -1)

