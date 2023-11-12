# 插入排序，往有序序列里插元素
# 最右边一对有问题的数字，是肯定要一次的


import sys
sys.stdin = open("sleepy.in", "r")
sys.stdout = open("sleepy.out", "w")

n = int(input())
cows = list(map(int, input().split()))

for i in range(1,n)[::-1]:  # 要找最右的
    if cows[i] < cows[i-1]:
        print(i)
        exit()
print(0)


