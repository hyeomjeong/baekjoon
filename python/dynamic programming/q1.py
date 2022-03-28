from sys import stdin

if __name__ == '__main__':
    t = int(stdin.readline().rstrip())
    for _ in range(t):
        k = int(stdin.readline().rstrip())
        pages = [map(int, stdin.readline().split())]
        res = 0

