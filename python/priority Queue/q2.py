from sys import stdin
import heapq
if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    plus_heap = [] #양수
    minus_heap = [] #음수
    for _ in range(N):
        n = int(stdin.readline().rstrip())
        if n == 0:
            m = heapq.heappop(minus_heap) if len(minus_heap) > 0 else 100000
            p = heapq.heappop(plus_heap) if len(plus_heap) > 0 else 100000
            if m == p:
                if m != 100000:
                    print(-m)
                    heapq.heappush(plus_heap, p)
                else:
                    print(0)
            elif m < p:
                print(-m)
                if p != 100000:
                    heapq.heappush(plus_heap, p)
            else:
                print(p)
                if m != 100000:
                    heapq.heappush(minus_heap, m)
        elif n > 0:
            heapq.heappush(plus_heap, n)
        else:
            heapq.heappush(minus_heap, -n)