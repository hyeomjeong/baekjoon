from sys import stdin

if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    A = list(map(int, stdin.readline().split()))
    stack = [0]
    NGE = [-1 for _ in range(N)]
    i = 1
    while stack and i < N:
        while stack and A[stack[-1]] < A[i]:
            NGE[stack[-1]] = A[i]
            stack.pop()
        stack.append(i)
        i += 1

    print(" ".join(map(str, NGE)))