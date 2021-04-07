from sys import stdin

if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    sequence = [int(stdin.readline().rstrip()) for _ in range(n)]
    stack = []
    res_msg = []
    res = []
    pos = 0
    i = 1
    while i <= n:
        if len(stack) > 0 and stack[-1] > i :
            print("NO")
            exit()

        if len(stack) > 0 and sequence[pos] == stack[-1] :
            res.append(stack.pop())
            res_msg.append("-")
            pos += 1
        else:
            stack.append(i)
            res_msg.append("+")
            i += 1

    while True:
        if len(stack) == 0:
            break
        res.append(stack.pop())
        res_msg.append("-")

    print("\n".join(res_msg) if res == sequence else "NO")