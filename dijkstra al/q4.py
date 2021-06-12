from sys import stdin
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if current_distance > distances[current_destination]:
            continue
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances


if __name__ == '__main__':
    T = int(stdin.readline().rstrip())
    for _ in range(T):
        n, m, t = map(int, stdin.readline().split()) # t 中 1
        s, g, h = map(int, stdin.readline().split()) # s = start
        adj_list = {x: {} for x in range(1, n + 1)}
        road = 0
        for _ in range(m):
            a, b, d = map(int, stdin.readline().split())
            if (a == g and b == h) or (a == h and b == g):
                road = d
            adj_list[a][b] = d if b not in adj_list[a].keys() else min(d, adj_list[a][b])
            adj_list[b][a] = d if a not in adj_list[b].keys() else min(d, adj_list[b][a])

        s_distances = dijkstra(adj_list, s)
        g_distances = dijkstra(adj_list, g)
        h_distances = dijkstra(adj_list, h)
        #print(g_distances, h_distances)
        t_list = [int(stdin.readline().rstrip()) for _ in range(t)]
        result = []
        for tmp in t_list:
            if s_distances[tmp] == float('inf') or g_distances[tmp] == float('inf') or h_distances[tmp] == float('inf'):
                continue
            gh_total = s_distances[g] + road + h_distances[tmp]
            hg_total = s_distances[h] + road + g_distances[tmp]
            if s_distances[tmp] == gh_total or s_distances[tmp] == hg_total:
                result.append(tmp)
        result.sort()
        print(" ".join(map(str, result)))
