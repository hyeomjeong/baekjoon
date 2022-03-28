from sys import stdin

def getGCD(a, b):
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a

if __name__ == '__main__':
    num1, num2 = map(int, stdin.readline().split())
    gcd = getGCD(num1, num2)
    print("%d\n%d" % (gcd, gcd * (num1/gcd) * (num2/gcd)))