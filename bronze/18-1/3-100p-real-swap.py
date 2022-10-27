# 统计个数就行

# 783410
# 618268
# 783410

# 相等那肯定就是中间那一个有问题，那小的就放前面

# 但其实没必要真的做交换
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
        i = i + 1

bessie_index = i

if flag == GO_RIGHT:
    while bessie_index+1 < len(lst):
        j = bessie_index + 1
        while j+1 < len(lst) and lst[j] == lst[j+1]:
            j += 1
        if lst[bessie_index] > lst[j]:
            lst[bessie_index], lst[j] = lst[j], lst[bessie_index]
            ans += 1
        bessie_index = j
else:
    while bessie_index-1 >= 0:
        j = bessie_index - 1
        while j - 1 >= 0 and lst[j] == lst[j-1]:
            j -= 1
        if lst[bessie_index] < lst[j]:
            lst[bessie_index], lst[j] = lst[j], lst[bessie_index]
            ans += 1
        bessie_index = j


print(ans)