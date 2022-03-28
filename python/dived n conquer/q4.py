from sys import stdin
import math

if __name__ == '__main__':
    A, B, C = map(int, stdin.readline().split())
    temp = 1

    while B > 1:
        if B % 2 != 0:
            B -= 1
            temp *= A % C

        while B % 2 == 0:
            A *= A % C
            B //= 2

    print(temp * A % C)

