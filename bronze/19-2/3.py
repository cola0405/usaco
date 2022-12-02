# 铜级题不会特别复杂！

# 先将问题简单化，分成两个问题
# 那要求两个问号的值的话，就是得分别往两边推

# range_low是指最小可以是多少
# range_high是指最大可以是多少

# 当两个none挨着的时候，该怎么确定current_flow呢
# 每个sensor都是准确的
# 也就是说应该取交集，不然就违反题意了！好好理解这一点
# 收缩的都可以用便利

# 用题目给的测试用例好好理解以上说的内容

# 范围的话，最小的low，最大的high
# none none的话，取交集
# 做减法的时候注意保证大于0


import sys
sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")

TYPE = 0
LOW = 1
HIGH = 2

sensors = []
n = int(input())
for i in range(n):
    t, low, high = input().split()
    sensors.append([t, int(low), int(high)])

# mile 1
# from right to left
current_low = 0
current_high = 0
for i in range(len(sensors))[::-1]:
    if sensors[i][TYPE] == 'none':
        current_low = sensors[i][LOW]
        current_high = sensors[i][HIGH]
        i -= 1
        # update
        while i >= 0:
            if sensors[i][TYPE] == 'none':
                current_low = max(current_low, sensors[i][LOW])
                current_high = min(current_high, sensors[i][HIGH])
            elif sensors[i][TYPE] == 'on':
                current_low = max(current_low - sensors[i][HIGH], 0)
                current_high = max(current_high - sensors[i][LOW], 0)
            elif sensors[i][TYPE] == 'off':
                current_low += sensors[i][LOW]
                current_high += sensors[i][HIGH]
            i -= 1
        break
print(current_low, current_high)

# mile n
current_low = 0
current_high = 0
for i in range(len(sensors)):
    if sensors[i][TYPE] == 'none':
        current_low = sensors[i][LOW]
        current_high = sensors[i][HIGH]
        i += 1
        # update
        while i < n:
            if sensors[i][TYPE] == 'none':
                current_low = max(current_low, sensors[i][LOW])
                current_high = min(current_high, sensors[i][HIGH])
            elif sensors[i][TYPE] == 'on':
                current_low += sensors[i][LOW]
                current_high += sensors[i][HIGH]
            elif sensors[i][TYPE] == 'off':
                current_low = max(current_low - sensors[i][HIGH], 0)
                current_high = max(current_high - sensors[i][LOW], 0)
            i += 1
        break
print(current_low, current_high)