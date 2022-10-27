# 统计个数就行

# 783410
# 618268
# 783410

# 相等那肯定就是中间那一个有问题，那小的就放前面

# 没必要真的做交换
# 写if条件的时候一定注意是否取等号，因为这影响到次数是否会多1少1

GO_LEFT = 0
GO_RIGHT = 1

import sys
sys.stdin = open('outofplace.in', 'r')
sys.stdout = open('outofplace.out', 'w')

lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))

flag = GO_LEFT
ans = 0
i = len(lst) - 1

# 判断方向
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        if i+2<len(lst) and lst[i] > lst[i+2]:
            flag = GO_RIGHT
            break
        # 相等那肯定就是中间那一个有问题，那小的就放前面
        elif i+2<len(lst) and lst[i] <= lst[i+2]:
            i = i + 1
            flag = GO_LEFT
            break
        # 这个处理很重要，是确定出问题的index
        i = i + 1

bessie = lst[i]

if flag == GO_RIGHT:
    while i+1 < len(lst):
        j = i+1
        while j+1 < len(lst) and lst[j] == lst[j+1]:
            j += 1
        ans += 1
        # 要取等号，因为下一项如果是等于的， 也不用继续换下去了
        if bessie <= lst[j+1]:
            break
        i = j
else:
    while i-1 >= 0:
        j = i-1
        while j-1 >= 0 and lst[j] == lst[j-1]:
            j -= 1
        ans += 1
        if bessie >= lst[j-1]:
            break
        i = j


print(ans)