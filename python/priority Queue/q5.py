def solution(n, k, cmd):
    table = [x for x in range(n)]
    curr_pos = k
    del_data = []

    for c in cmd:
        cs = c.split()
        if len(cs) > 1:
            # 현재 선택된 행에서 X칸 아래
            if cs[0] == "D":
                curr_pos += cs[1]
            # X 칸 위
            else:
                curr_pos -= cs[1]
        else:
            if cs[0] == "C":
                del_data.append([table[curr_pos], curr_pos])
                table.remove(curr_pos)
                if curr_pos == len(table):
                    curr_pos -= 1
            else:
                data = del_data.pop()
                if data[1] > len(table):
                    table.append(data[0])
                else:
                    table.insert(data[1], data[0])
    answer = ""
    for x in range(n):
        if x in del_data:
            answer += "X"
        else:
            answer += "O"

    return answer

if __name__ == '__main__':
    solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])