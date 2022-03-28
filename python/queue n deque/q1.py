from sys import stdin
from collections import deque

if __name__ == '__main__':
    loop = int(stdin.readline().rstrip())

    arr_list = deque()
    for _ in range(loop):
        command = stdin.readline().split()
        if len(command) > 1:
            arr_list.append(command[1])
        else:
            c = command[0]
            if c == "front":
                print(arr_list[0] if len(arr_list) > 0 else -1)
            elif c == "back":
                print(arr_list[-1] if len(arr_list) > 0 else -1)
            elif c == "size":
                print(len(arr_list))
            elif c == "empty":
                print(0 if len(arr_list) > 0 else 1)
            else:
                print(arr_list.popleft() if len(arr_list) > 0 else -1)