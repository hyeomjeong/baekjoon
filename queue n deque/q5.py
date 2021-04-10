from sys import stdin
from collections import deque

if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    dq = deque()
    for _ in range(n):
        command = stdin.readline().split()
        if len(command) > 1:
            if command[0] == "push_back":
                dq.append(command[1])
            else:
                dq.appendleft(command[1])
        else:
            if command[0] == "front":
                print(dq[0] if len(dq) > 0 else -1)
            elif command[0] == "back":
                print(dq[-1] if len(dq) > 0 else -1)
            elif command[0] == "pop_front":
                print(dq.popleft() if len(dq) > 0 else -1)
            elif command[0] == "pop_back":
                print(dq.pop() if len(dq) > 0 else -1)
            elif command[0] == "size":
                print(len(dq))
            else:
                print(1 if len(dq) == 0 else 0)