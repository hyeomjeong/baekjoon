from sys import stdin

res = [0, 0, 0]

def checkPaper(start_r, end_r, start_c, end_c, arr):
    global res

    temp = arr[start_r][start_c]

    for r in range(start_r, end_r):
        for c in range(start_c, end_c):
            if temp != arr[r][c]:
                # top left
                checkPaper(start_r, start_r + ((end_r - start_r) // 3), start_c, start_c + ((end_c - start_c) // 3), arr)
                # top center
                checkPaper(start_r, start_r + ((end_r - start_r) // 3), start_c + ((end_c - start_c) // 3), start_c + ((end_c - start_c) // 3 * 2), arr)
                # top right
                checkPaper(start_r, start_r + ((end_r - start_r) // 3), start_c + ((end_c - start_c) // 3 * 2), end_c, arr)
                # left
                checkPaper(start_r + ((end_r - start_r) // 3), start_r + ((end_r - start_r) // 3 * 2), start_c, start_c + ((end_c - start_c) // 3), arr)
                # center
                checkPaper(start_r + ((end_r - start_r) // 3), start_r + ((end_r - start_r) // 3 * 2), start_c + ((end_c - start_c) // 3), start_c + ((end_c - start_c) // 3 * 2), arr)
                # right
                checkPaper(start_r + ((end_r - start_r) // 3), start_r + ((end_r - start_r) // 3 * 2), start_c + ((end_c - start_c) // 3 * 2), end_c, arr)
                # bottom left
                checkPaper(start_r + ((end_r - start_r) // 3 * 2), end_r, start_c, start_c + ((end_c - start_c) // 3), arr)
                # bottom
                checkPaper(start_r + ((end_r - start_r) // 3 * 2), end_r, start_c + ((end_c - start_c) // 3), start_c + ((end_c - start_c) // 3 * 2), arr)
                # bottom right
                checkPaper(start_r + ((end_r - start_r) // 3 * 2), end_r, start_c + ((end_c - start_c) // 3 * 2), end_c, arr)
                return

    if temp == "0":
        res[1] += 1
    elif temp == "1":
        res[2] += 1
    else:
        res[0] += 1


if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    paper = [stdin.readline().split() for _ in range(N)]

    checkPaper(0, N, 0, N, paper)

    print("\n".join(map(str, res)))