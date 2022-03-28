from sys import stdin

def getFac(N, K):
    if N == K or N < 2 or K == 0:
        return 1
    return getFac(N-1, K) * N

if __name__ == '__main__':
    T = int(stdin.readline().rstrip())

    for _ in range(T):
        n, m = map(int, stdin.readline().split())
        print(getFac(m, n) // getFac(m - n, 1))
