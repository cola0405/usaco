BLOCKED = False
UNBLOCKED = True


def checkRow(path, row, start, end):
    current_col = start
    while current_col < end:
        if path[row][current_col] == 'H':
            return BLOCKED
        current_col += 1
    else:
        return UNBLOCKED


def checkColumn(path, column, start, end):
    current_row = start
    while current_row < end:
        if path[current_row][column] == 'H':
            return BLOCKED
        current_row += 1
    else:
        return UNBLOCKED


round = int(input())
ans = []
for r in range(round):
    n, k = map(int, input().split(" "))
    path = []
    for row in range(n):
        path.append(input())
    ans = 0
    home = n - 1
    if k >= 1:
        # go right at first
        if checkRow(path, 0, 0, home) \
                and checkColumn(path, n - 1, 0, home):
            ans += 1
        # go down at first
        if checkColumn(path, 0, 0, n - 1) \
                and checkRow(path, n - 1, 1, home):
            ans += 1
    print('k=1', ans)
    if k >= 2:
        # go right at first
        for current_col in range(1, n - 1):
            if checkColumn(path, current_col, 0, home) \
                    and checkRow(path, n - 1, current_col + 1, home):
                ans += 1
        # go down at first
        for current_row in range(1, n - 1):
            if checkRow(path, current_row, 0, home) \
                    and checkColumn(path, n-1, current_row + 1, home):
                ans += 1
    print('k=2', ans)
    if k >= 3:
        # go right at first
        for i in range(1, n-1):
            for j in range(1, n-1):
                if checkColumn(path, i, 0, j)\
                    and checkRow(path, j, i+1, n-1)\
                    and checkColumn(path, n-1, j+1, n-1):
                    ans += 1

        # go down at first
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if checkRow(path, i, 0, j) \
                        and checkColumn(path, i, i + 1, n - 1) \
                        and checkRow(path, n-1, j + 1, n - 1):
                    ans += 1
    print('k=3', ans)
    print(ans)
