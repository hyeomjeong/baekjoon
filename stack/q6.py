from sys import stdin

if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    A = list(map(int, stdin.readline().split()))

    NGE = [-1 for _ in range(N)]
    for idx in range(N):
        for i in range(idx+1, N):
            if A[idx] < A[i]:
                NGE[idx] = A[i]
                break
    print(" ".join(map(str, NGE)))