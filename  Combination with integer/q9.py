from sys import stdin

if __name__ == '__main__':
    tc = int(stdin.readline().rstrip())
    for _ in range(tc):
        n = int(stdin.readline().rstrip())
        clothes = {}
        for _ in range(n):
            name, kinds = stdin.readline().split()
            clothes[kinds] = clothes[kinds] + 1 if kinds in clothes.keys() else 1

        temp = 1
        for v in clothes.values():
            temp *= (v + 1)
        print(temp-1)