# 模拟 交换
# 类 shell game


import sys
sys.stdin = open("shuffle.in", 'r')
sys.stdout = open("shuffle.out", 'w')

n = int(input())
shuffle = list(map(int, input().split()))
ids = input().split()

for _ in range(3):
    temp = []
    for i in range(n):
        temp.append(ids[shuffle[i]-1])
    ids = temp

for i in ids:
    print(i)

