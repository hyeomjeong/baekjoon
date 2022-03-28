from sys import stdin

def getGCD(a, b):
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a


if __name__ == '__main__':
    tc = int(stdin.readline().rstrip())
    for _ in range(tc):
        num1, num2 = map(int, stdin.readline().split())
        gcd = getGCD(num1, num2)
        print(num1 * num2 // gcd)