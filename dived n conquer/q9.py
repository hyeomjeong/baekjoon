from sys import stdin
import math

def getMinChild(s, tree, arr, idx):
    if tree[idx] != 0:
        return
    if idx*2 > len(tree):
        return
    if tree[idx*2] == -1:
        getMinChild(s, tree, arr, idx*2)

    if tree[idx*2+1] == -1:
        getMinChild(s, tree, arr, idx*2+1)

    s[idx] = s[idx*2] + s[idx*2+1]
    tree[idx] = tree[idx*2+1] if ((arr[tree[idx*2]] > arr[tree[idx*2+1]]) and (tree[idx*2 + 1] != -1)) else tree[idx * 2]


# init
def init(arr):
    capacity = pow(2, math.ceil(math.log2(n)))
    tree = [0 for _ in range(capacity * 2)]
    for idx in range(capacity, capacity + n):
        tree[idx] = idx - capacity

    return tree


def getRes(arr):
    capacity = pow(2, math.ceil(math.log2(n)))
    min_tree = [-1 for _ in range(capacity * 2)]
    s = [0 for _ in range(capacity * 2)]
    for idx in range(capacity, capacity + n):
        min_tree[idx] = idx - capacity
        s[idx] = 1

    # get min of child
    getMinChild(s, min_tree, arr, 1)
    res = 0
    for idx in range(capacity*2):
        if min_tree[idx] != -1:
            res = max(res, arr[min_tree[idx]] * s[idx])

    return res


if __name__ == '__main__':
    while True:
        line = list(map(int, stdin.readline().split()))
        if len(line) == 1:
            break
        n = line[0]
        square = line[1:]

        while len(square) > 1:
            s_tree = init(square)






