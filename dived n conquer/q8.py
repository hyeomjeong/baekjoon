from sys import stdin
d_num = 1000000007

def mulMatrix(a, b):
    global d_num

    new_m = [[0, 0], [0, 0]]
    for r in range(2):
        for c in range(2):
            t = 0
            for i in range(2):
                t += a[r][i] * b[i][c] % d_num
            new_m[r][c] = t % d_num

    return new_m



if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    fib_matrix = [[1, 1], [1, 0]]
    temp = [[1, 0], [0, 1]]

    while n > 1:
        if n % 2 != 0:
            n -= 1
            temp = mulMatrix(temp, fib_matrix)

        while n % 2 == 0:
            n //= 2
            fib_matrix = mulMatrix(fib_matrix, fib_matrix)
    fib_matrix = mulMatrix(fib_matrix, temp)
    print(fib_matrix[0][1])


