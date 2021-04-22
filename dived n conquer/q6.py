from sys import stdin

if __name__ == '__main__':

    a_row, a_col = map(int, stdin.readline().split())
    a_matrix = [list(map(int, stdin.readline().split())) for _ in range(a_row)]
    b_row, b_col = map(int, stdin.readline().split())

    res_matrix = [[0] * b_col for _ in range(a_row)]

    for br in range(b_row):
        b_line = list(map(int, stdin.readline().split()))
        for ar in range(a_row):
            for bc in range(b_col):
                res_matrix[ar][bc] += a_matrix[ar][br] * b_line[bc]

    for r in range(a_row):
        print(" ".join(map(str, res_matrix[r])))
