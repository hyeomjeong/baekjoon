from sys import stdin


if __name__ == '__main__':
    cnt = int(stdin.readline().rstrip())
    divisors = list(map(int, stdin.readline().split()))
    divisors.sort()
    print(divisors[0] * divisors[-1])