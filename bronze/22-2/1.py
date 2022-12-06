# 没办法找到final line
# 转换思路

# 总和一定，枚举组数，得到每组的数
# 累加，一旦不符，则表示必不可行

t = int(input())
for _ in range(t):
    n = int(input())
    times = tuple(map(int, input().split()))
    s = sum(times)
    for group in range(1, n+1)[::-1]:
        if s%group == 0:
            amount = s//group
            tmp = 0
            for i in times:
                tmp += i
                if tmp > amount:
                    break
                if tmp == amount:
                    tmp = 0
            else:
                print(n - group)
                break
    else:
        print(n-1)
