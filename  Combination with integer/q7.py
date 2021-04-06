from sys import stdin

def getFac(n, k):
    if n == k:
        return 1
    if n < 2:
        return 1
    return getFac(n-1, k) * n

if __name__ == '__main__':
    n, k = map(int, stdin.readline().split())

    if 0 <= k <= n:
        print((getFac(n, k) // getFac(n-k, 1)) % 10007)
    else:
        print(0)
