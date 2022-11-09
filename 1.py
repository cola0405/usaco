with open("crosswords.in", "r") as reader:
    n, m = map(int, reader.readline().strip().split(" "))
    crossword = [reader.readline().strip() for _ in range(n)]


def horizontal(position, crossword, m):
    if position[1] - 1 < 0 or crossword[position[0]][position[1] - 1] == "#":
        if position[1] + 2 <= m - 1 and crossword[position[0]][position[1] + 1] == "." and crossword[position[0]][position[1] + 2] == ".":
            return True
    return False


def vertical(position, crossword, n):
    if position[0] - 1 < 0 or crossword[position[0] - 1][position[1]] == "#":
        if position[0] + 2 <= n - 1 and crossword[position[0] + 1][position[1]] == "." and crossword[position[0] + 2][position[1]] == '.':
            return True
    return False


def crosswords(n, m, crossword):
    res = 0
    ans = []
    for y in range(n):
        for x in range(m):
            if crossword[y][x] == ".":
                if vertical([y, x], crossword, n) or horizontal([y, x], crossword, m):
                    res += 1
                    ans.append([y + 1, x + 1])
    return [res, ans]


with open("crosswords.out", "w") as writer:
    fout = crosswords(n, m, crossword)
    writer.write(str(fout[0]))
    writer.write("\n")
    for i in range(fout[0]):
        val = ""
        val += str(fout[1][i][0])
        val += " "
        val += str(fout[1][i][1])
        val += "\n"
        writer.write(val) 