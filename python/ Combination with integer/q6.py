from sys import stdin

def getGCD(a, b):
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a


if __name__ == '__main__':
    ring = int(stdin.readline().rstrip())
    rs = list(map(int, stdin.readline().split()))
    standard_r = rs[0]

    for idx in range(1, ring):
        r = rs[idx]
        gcd = getGCD(standard_r, r)
        print("%d/%d" % ( standard_r // gcd, r // gcd))


