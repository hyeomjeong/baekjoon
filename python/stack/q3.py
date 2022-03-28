from sys import stdin

if __name__ == '__main__':
    loop = int(stdin.readline().rstrip())
    for _ in range(loop):
        stack = []
        msg = stdin.readline().rstrip()
        for item in msg:
            if item == ")":
                if len(stack) == 0:
                    stack.append(item)
                    break
                stack.pop()
            else:
                stack.append(item)
        print("NO" if len(stack) > 0 else "YES")
