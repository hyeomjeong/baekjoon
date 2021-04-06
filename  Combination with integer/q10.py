from sys import stdin

def getZero(n):
    if n < 5:
        return 0
    zero_cnt = n // 5
    return getZero(n // 5) + zero_cnt

if __name__ == '__main__':
    num = int(stdin.readline().rstrip())
    print(getZero(num))