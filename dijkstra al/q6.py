from sys import stdin

if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    m = int(stdin.readline().rstrip())
    adj_table = [[float('inf')] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        adj_table[a-1][b-1] = min(c, adj_table[a-1][b-1])
    for idx in range(n):
        adj_table[idx][idx] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj_table[i][k] + adj_table[k][j] < adj_table[i][j]:
                    adj_table[i][j] = adj_table[i][k] + adj_table[k][j]

    for t in adj_table:
        print(" ".join(map(lambda x: "0" if x == float('inf') else str(x), t)))