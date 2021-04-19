from sys import stdin

res = ""

def compress(start_r, end_r, start_c, end_c, arr):
    global res
    temp = arr[start_r][start_c]

    for r in range(start_r, end_r):
        for c in range(start_c, end_c):
            if temp != arr[r][c]:
                res += "("
                # top left
                compress(start_r, (start_r + end_r) // 2, start_c, (start_c + end_c) // 2, arr)
                # top right
                compress(start_r, (start_r + end_r) // 2, (start_c + end_c) // 2, end_c, arr)
                # bottom left
                compress((start_r + end_r) // 2, end_r, start_c, (start_c + end_c) // 2, arr)
                # bottom right
                compress((start_r + end_r) // 2, end_r, (start_c + end_c) // 2, end_c, arr)
                res += ")"
                return
    res += temp


if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    video = [stdin.readline().rstrip() for _ in range(N)]

    compress(0, N, 0, N, video)
    print(res)
