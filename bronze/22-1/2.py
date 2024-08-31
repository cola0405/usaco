def win(d1, d2):
    # 模拟所有对局情况 -- 如果赢的多则 d1 more likely win d2
    w,l = 0,0       
    for num1 in d1:
        for num2 in d2:
            if num1 > num2:
                w += 1
            elif num1 < num2:
                l += 1
    return w > l

def solve():
    line = list(map(int, input().split()))
    a = line[:4]
    b = line[4:]
    for c1 in range(1, 11):      # 模拟c_dice的所有情况
        for c2 in range(1, 11):
            for c3 in range(1, 11):
                for c4 in range(1, 11):
                    c = (c1, c2, c3, c4)

                    # 检查是否为 Non-Transitive Dice
                    if (win(a, b) and win(b, c) and win(c, a))\
                        or (win(b, a) and win(a, c) and win(c, b)):
                        print('yes')
                        return
    print('no')

n = int(input())
for r in range(n):
    solve()
