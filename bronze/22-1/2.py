def win(d1, d2):
    w,l = 0,0  # 模拟所有对局情况 -- 如果赢得多则X more likely win Y
    for num1 in d1:
        for num2 in d2:
            if num1 > num2:
                w += 1
            elif num1 < num2:
                l += 1
    return w > l

def solve():
    line = list(map(int, input().split()))
    a_die = line[:4]
    b_die = line[4:]
    for a in range(1, 11):      # 模拟c_dice的所有情况
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                    c_die = (a, b, c, d)

                    # 检查可行的情况
                    if win(a_die, b_die) and win(b_die, c_die) and win(c_die, a_die):
                        print('yes')
                        return
                    if win(b_die, a_die) and win(a_die, c_die) and win(c_die, b_die):
                        print('yes')
                        return
    print('no')

n = int(input())
for r in range(n):
    solve()
