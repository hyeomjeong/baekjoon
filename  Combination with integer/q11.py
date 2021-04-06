from sys import stdin

count5 = 0

def fac(n):
    global count5
    while n > 1:
        if n % 5 != 0:
            break
        if n % 5 == 0:
            count5 += 1
            n //= 5


if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    for i in range(1, N+1):
        fac(i)
    print(count5)