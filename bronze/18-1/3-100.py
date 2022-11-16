# 有序序列
# no need to do the real swap
# 模拟

import sys
sys.stdin = open('outofplace.in', 'r')
sys.stdout = open('outofplace.out', 'w')

GO_LEFT = 0
GO_RIGHT = 1

lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))

bessie_index = 0
flag = GO_LEFT

# find bessie
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        if i+2 >= len(lst):
            bessie_index = i + 1
            flag = GO_LEFT
            break
        if lst[i] > lst[i+2]:
            bessie_index = i
            flag = GO_RIGHT
            break
        elif lst[i] <= lst[i+2]:
            bessie_index = i+1
            flag = GO_LEFT
            break


s = set()
if flag == GO_LEFT:
    for i in range(bessie_index):
        if lst[i] > lst[bessie_index]:
            s.add(lst[i])
else:
    for i in range(bessie_index, len(lst)):
        if lst[i] < lst[bessie_index]:
            s.add(lst[i])

print(len(s))



