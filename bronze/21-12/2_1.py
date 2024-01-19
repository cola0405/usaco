# 根据2.py 的思路分析比较容易想到的一种实现是下面这样的

n = int(input())
target = list(map(int, input().split()))
origin = list(map(int, input().split()))

ans = 0
i = 0
last = 0
while i<n:
    diff = target[i] - origin[i]
    if diff * last > 0:  # 可以跟一部分
        ans += abs(diff) - abs(last)
    else:
        ans += abs(diff)
    j = i

    # while 循环查看哪些能贪
    while j+1<n:
        next_diff = target[j+1] - origin[j+1]
        if next_diff*diff > 0 and abs(next_diff) <= abs(diff):  # abs 是为了处理负数
            diff = next_diff
            j += 1
        else:       # 只要遇到反方向的或者更高的，则没办法贪下去
            break
    last = diff     # 保留的last就是可以跟的那一部分
    i = j+1

print(ans)

'''
5
1 2 -1 -2 3
0 0 0 0 0

'''


