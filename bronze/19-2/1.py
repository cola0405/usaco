# 题意需要注意一个规则：
# 每次只能移动两端的cow，且只能把cow放到另外两头cows中间

# min 比较简单，只能是0次，1次，2次（无论在何位置，最多两次就能放好）
# max 滚刀肉
# 测试用例：1 7 9
# 1 6 7
# 1 5 6
# 1 4 5
# 1 3 4
# 1 2 3
# ans：5

import sys
sys.stdin = open('herding.in', 'r')
sys.stdout = open('herding.out', 'w')

a,b,c = sorted(map(int, input().split()))
if a+1==b and b+1==c:
    min_op = 0
elif c-b==2 or b-a==2:
    min_op = 1
else:
    min_op = 2

gap1 = b-a
gap2 = c-b
max_op = max(gap1,gap2)-1

print(min_op)
print(max_op)




