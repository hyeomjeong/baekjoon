from sys import stdin

if __name__ == '__main__':
    loop = int(stdin.readline().rstrip())
    stack = []
    for _ in range(loop):
        command = stdin.readline().split()
        if len(command) > 1:
            stack.append(command[1])
        else:
            c = command[0]
            if c == "top" :
                print(stack[-1] if len(stack) > 0 else -1)
            elif c == "size" :
                print(len(stack))
            elif c == "empty" :
                print(0 if len(stack) > 0 else 1)
            else:
                print(stack.pop() if len(stack) > 0 else -1)