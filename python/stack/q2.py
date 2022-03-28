from sys import stdin

if __name__ == '__main__':
    K = int(stdin.readline().rstrip())
    numbers = []
    for _ in range(K):
        n = int(stdin.readline().rstrip())
        if n == 0:
            numbers.pop()
        else:
            numbers.append(n)
    print(sum(numbers))