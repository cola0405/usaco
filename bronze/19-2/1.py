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
sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

min_ans = 0
max_ans = 0

loc = list(map(int, input().split()))
loc.sort()
max_gap0 = loc[2] - loc[0]
max_gap1 = loc[2] - loc[1]
min_gap1 = loc[1] - loc[0]
min_gap2 = loc[2] - loc[0]

if max_gap1 == 1 and max_gap0 == 2:
    min_ans = 0
elif max_gap1 == 2 \
        or min_gap1 == 2:
    min_ans = 1
else:
    min_ans = 2
max_ans = max(min_gap1, max_gap1) - 1

print(min_ans)
print(max_ans)




