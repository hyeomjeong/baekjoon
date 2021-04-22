from sys import stdin

c = 1000000007
def binomial(n, k, dp):
    global c
    if n == k or k == 0:
        return 1 % c
    if dp[n][k] == 0:
        dp[n][k] = binomial(n-1, k-1, dp) + binomial(n-1, k, dp)
    return dp[n][k] % c



if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())

    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    binomial()
