from sys import stdin
import heapq

if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    heap = []
    for i in range(1, N+1):
        heapq.heappush(heap, int(stdin.readline().rstrip()))
        l = i // 2
        temp_h = heap.copy()
        temp = heapq.heappop(temp_h)
        for j in range(1, l+1):
            temp = heapq.heappop(temp_h)
        print(min(temp, heapq.heappop(temp_h)) if l % 2 == 0 else temp)


