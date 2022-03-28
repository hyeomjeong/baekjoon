from sys import stdin

if __name__ == '__main__':
    N = int(stdin.readline().rstrip())
    conferences = [list(map(int, stdin.readline().split())) for _ in range(N)]
    # sort by end time
    conferences.sort(key=lambda x: (x[1], x[0]))
    cnt = 0
    end = 0
    for con in conferences:
        if con[0] >= end:
            end = con[1]
            cnt += 1
    print(cnt)
