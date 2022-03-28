from sys import stdin
from collections import deque
if __name__ == '__main__':
    tc = int(stdin.readline().rstrip())

    for _ in range(tc):
        n, pos = map(int, stdin.readline().split())
        p_list = list(map(int, stdin.readline().split()))
        p_idx = deque(x for x in range(n))
        cnt = 1
        while True:
            max_p = max(p_list)
            while p_list[p_idx[0]] != max_p:
                p_idx.append(p_idx.popleft())
            if p_idx[0] == pos:
                print(cnt)
                break
            p_list[p_idx[0]] = 0
            cnt += 1



