from sys import stdin


def mulMatrix(a, b):
    new_matrix = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            t = 0
            for i in range(N):
                t += a[i][c] * b[r][i] % 1000
            new_matrix[r][c] = t % 1000

    return new_matrix


if __name__ == '__main__':
    N, B = map(int, stdin.readline().split())

    temp = [[0] * N for _ in range(N)]
    for idx in range(N):
        temp[idx][idx] = 1

    matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]

    while B > 1:
        if B % 2 != 0:
            B -= 1
            temp = mulMatrix(temp, matrix)
        while B % 2 == 0:
            B //= 2
            matrix = mulMatrix(matrix, matrix)

    matrix = mulMatrix(temp, matrix)

    for idx in range(N):
        print(" ".join(map(str, matrix[idx])))