from sys import stdin

def getRelation(a, b):
    if a % b == 0:
        return "multiple"
    if b % a == 0:
        return "factor"
    return "neither"


if __name__ == '__main__':
    while True:
        num1, num2 = map(int, stdin.readline().split())
        if num1 == 0 and num2 == 0:
            break
        print(getRelation(num1, num2))


