from sys import stdin

if __name__ == '__main__':
    msg = stdin.readline().rstrip()
    while msg != ".":
        stack = []
        for item in msg:
            if item == "[" or item == "(":
                stack.append(item)
            elif item == "]" or item == ")":
                if len(stack) == 0:
                   stack.append(item)
                   break
                else:
                    if ord(stack[-1]) + 1 == ord(item) or ord(stack[-1]) + 2 == ord(item):
                        stack.pop()
                    else:
                        stack.append(item)
            elif item == ".":
                break
        print("no" if len(stack) > 0 else "yes")

        msg = stdin.readline().rstrip()