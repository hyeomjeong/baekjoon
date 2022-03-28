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
    n, e = map(int, stdin.readline().split())
    adj_list = {x: {} for x in range(1, n+1)}
    for _ in range(e):
        a, b, c = map(int, stdin.readline().split())
        adj_list[a][b] = c if b not in adj_list[a].keys() else min(c, adj_list[a][b])
        adj_list[b][a] = c if a not in adj_list[b].keys() else min(c, adj_list[b][a])
    v1, v2 = map(int, stdin.readline().split())
    start_distances = dijkstra(adj_list, 1)
    if v1 == 1:
        if v2 == n:
            res = start_distances[n]
        else:
            v2_distances = dijkstra(adj_list, v2)
            res = start_distances[v2] + v2_distances[n]
    elif v1 != 1 and v2 == n:
        v1_distances = dijkstra(adj_list, v1)
        res = start_distances[v1] + v1_distances[n]
    else:
        v1_distances = dijkstra(adj_list, v1)
        v2_distances = dijkstra(adj_list, v2)
        v1_total = start_distances[v1] + v1_distances[v2] + v2_distances[n]
        v2_total = start_distances[v2] + v2_distances[v1] + v1_distances[n]
        res = min(v1_total, v2_total)
    print(res if res != float('inf') else -1)
