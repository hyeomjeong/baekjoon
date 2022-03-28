from sys import stdin

white_cnt = 0
blue_cnt = 0


def checkPaper(start_r, start_c, end_r, end_c, arr):
    global white_cnt, blue_cnt

    if start_r == end_r - 1 and start_c == end_c - 1:
        if arr[start_r][start_c] == 1:
            blue_cnt += 1
        else:
            white_cnt += 1
        return

    temp = arr[start_r][start_c]

    for row in range(start_r, end_r):
        for col in range(start_c, end_c):
            if temp != arr[row][col]:
                # 1
                checkPaper(start_r, start_c, (start_r + end_r) // 2, (start_c + end_c) // 2, arr)
                # 2
                checkPaper(start_r, (start_c + end_c) // 2, (start_r + end_r) // 2, end_c, arr)
                # 3
                checkPaper((start_r + end_r) // 2, start_c, end_r, (start_c + end_c) // 2, arr)
                # 4
                checkPaper((start_r + end_r) // 2, (start_c + end_c) // 2, end_r, end_c, arr)
                return

    if temp == 1:
        blue_cnt += 1
    else:
        white_cnt += 1


if __name__ == '__main__':

    N = int(stdin.readline().rstrip())
    paper = []
    # insert color paper
    for _ in range(N):
        paper.append(list(map(int, stdin.readline().split())))

    # get cnts
    checkPaper(0, 0, N, N, paper)

    print("%d\n%d" % (white_cnt, blue_cnt))
