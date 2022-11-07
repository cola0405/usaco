BLOCKED = False
UNBLOCKED = True

RIGHT = 0
DOWN = 1

record = [None]*50
record = [record]*50
record = [record]*2


def checkRow(row, column):
    if record[RIGHT][row][column] != None:
        return record[RIGHT][row][column]
    end = n-1
    while column <= end:
        if path[row][column] == 'H':
            record[RIGHT][row][column] = BLOCKED
            return BLOCKED
        column += 1
    else:
        record[RIGHT][row][column] = UNBLOCKED
        return UNBLOCKED



def checkColumn(row, column):
    if record[DOWN][row][column] != None:
        return record[DOWN][row][column]
    end = n-1
    while row <= end:
        if path[row][column] == 'H':
            record[DOWN][row][column] = BLOCKED
            return BLOCKED
        row += 1
    else:
        record[DOWN][row][column] = UNBLOCKED
        return UNBLOCKED



round = int(input())
for r in range(round):
    n, k = map(int, input().split(" "))
    path = []
    for row in range(n):
        path.append(input())
    ans1 = 0
    end = n - 1
    if k >= 1:
        # go right at first
        if checkRow(0, 0) \
                and checkColumn(0, end):
            ans1 += 1
        # go down at first
        if checkColumn(0, 0) \
                and checkRow(end, 0):
            ans1 += 1
    ans2 = 0
    if k >= 2:
        # go right at first
        for column in range(1, end):
            if path[0][column] == 'H':
                break
            if checkColumn(0, column) \
                    and checkRow(end, column):
                ans2 += 1
        # go down at first
        for current_row in range(1, end):
            if path[current_row][0] == 'H':
                break
            if checkRow(current_row, 0) \
                    and checkColumn(current_row, end):
                ans2 += 1
    ans3 = 0
    if k >= 3:
        # go right at first
        for column in range(1, n-1):
            if path[0][column] == 'H':
                break
            for row in range(1, n-1):
                if path[row][column] == 'H':
                    break
                if checkRow(row, column)\
                    and checkColumn(row, end):
                    ans3 += 1

        # go down at first
        for row in range(1, end):
            if path[row][0] == 'H':
                break
            for column in range(1, n - 1):
                if path[row][column] == 'H':
                    break
                if checkColumn(row, column) \
                        and checkRow(end, column):
                    ans3 += 1
    ans = ans1+ans2+ans3
    print(ans1,ans2,ans3)
    print(ans)
