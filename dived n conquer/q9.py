from sys import stdin

if __name__ == '__main__':
    while True:
        line = list(map(int, stdin.readline().split()))
        if len(line) == 1:
            break
        n = line[0]
        squares = line[1:]
        res = 0
        for current_s in squares:
            stack = []
            for next_s in squares:
                if current_s <= next_s:
                    stack.append(next_s)
                else:
                    res = max(len(stack) * current_s, res)
                    stack = []

            if len(stack) > 0:
                res = max(len(stack) * current_s, res)
        print(res)

