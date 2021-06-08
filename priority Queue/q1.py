from sys import stdin
import heapq
if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    heap = []
    for _ in range(N):
        n = int(stdin.readline().rstrip())
        if n == 0:
            print(heapq.heappop(heap) if len(heap) > 0 else 0)
        else:
            heapq.heappush(heap, n)



