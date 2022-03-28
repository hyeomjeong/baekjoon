from sys import stdin

def getGCD(a, b) :
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

def getDiv(num):
    result = []
    if num % 2 == 0:
        result = [2]

    for i in range(3, num + 1, 2):
        if num % i == 0:
            result.append(i)

    return result

if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    numbers = [int(stdin.readline().rstrip()) for _ in range(N)]

    gcd = numbers[0]
    for idx in range(1, N):
        gcd = getGCD(gcd, numbers[idx])
    gcd_div = getDiv(gcd)

