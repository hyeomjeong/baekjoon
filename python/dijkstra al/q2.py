from sys import stdin
import heapq

def d(graph, start):
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
    V, E = map(int, stdin.readline().split())
    S = int(stdin.readline().rstrip())
    v_list = {x: {} for x in range(1, V+1)}

    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())
        v_list[u][v] = w if v not in v_list[u].keys() else min(w, v_list[u][v])

    print(d(v_list, S))