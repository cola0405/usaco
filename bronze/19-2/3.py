# range_low是指最小可以是多少
# range_high是指最大可以是多少

# 当两个none挨着的时候，该怎么确定current_flow呢
# 每个sensor都是准确的
# 也就是说应该取交集，不然就违反题意了！好好理解这一点

# 这里我换一个问题，你不用管1-mile，我就单纯问你n-mile时的预测
# 是不是应该从左往右更新


# 对于1-mile而言，需要从右往左反推，这一点应该是没有疑问的
# 但从哪开始？
# 从右往左第一个none
# 不能从最左边的none开始，如果这样局部取值的话
# 对于其他sensor可能会违反题意
# 必须从右往左推过来（与n-mile为什么要从左往右推同理）

# 用题目给的测试用例好好理解以上说的内容


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
current_low = 0
current_high = 0
for i in range(len(sensors))[::-1]:
    if sensors[i][TYPE] == 'none':
        current_low = sensors[i][LOW]
        current_high = sensors[i][HIGH]
        i -= 1
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