from sys import stdin
from collections import deque

if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    circle = deque(x for x in range(1, N+1))
    result = []
    while len(circle) > 0:
        for _ in range(K-1):
            circle.append(circle.popleft())
        result.append(circle.popleft())
    print("<%s>" % (", ".join(map(str, result))))