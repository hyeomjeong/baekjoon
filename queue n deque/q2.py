from sys import stdin
from collections import deque

if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    cards = deque(x for x in range(1, N+1))
    while True:
        if len(cards) > 1:
            cards.popleft()
        else:
            print(cards.pop())
            break
        cards.append(cards.popleft())