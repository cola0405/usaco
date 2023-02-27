t = int(input())

def clockwise_90(s):
    res = []
    k = len(s)
    for i in range(k):
        res.append([0] * k)

    for i in range(k):
        for j in range(k):
            res[j][k-1 - i] = s[i][j]
    return res


def draw(stamp, canvas, i, j):
    # 如果没有不合格的，从canvas下手，转！
    flag = True
    for di in range(K):
        for dj in range(K):
            if stamp[di][dj] == "*" and canvas[i+di][j+dj] == ".":
                flag = False
                break
        if flag == False:
            break
    else:
        # if no mistake, turn * to !
        for di in range(K):
            for dj in range(K):
                if canvas[i+di][j+dj] == "*" and stamp[di][dj] == "*":
                    canvas[i+di][j+dj] = "!"

for _ in range(t):
    input()
    N = int(input())
    canvas = []
    correct_amount = 0
    for r in range(N):
        line = list(input())
        canvas.append(line)
        correct_amount += line.count("*")

    K = int(input())
    stamp = []
    for r in range(K):
        line = list(input())
        stamp.append(line)

    # 旋转算法
    stamps = [stamp]
    for i in range(3):
        stamps.append(clockwise_90(stamps[-1]))

    # 遍历canvas
    for i in range(N):
        for j in range(N):
            # 四个都试着印一遍，一旦有出格的就舍弃

            # ps：stamp不允许出界
            if j+K-1>=N or i+K-1 >= N:
                continue

            # 画就完了
            for stamp in stamps:
                draw(stamp, canvas, i, j)

    # check ! amount
    amount = 0
    for line in canvas:
        amount += line.count("!")
    if amount == correct_amount:
        print("YES")
    else:
        print("NO")


# 1
#
# 3
# .**
# .**
# ***
# 3
# ...
# ...
# ***