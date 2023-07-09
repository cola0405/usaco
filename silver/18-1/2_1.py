# 贪心策略是 -- 肯定产奶量高的奶牛拿去卖奶，低的拿去租
# 排序，然后前n头牛拿去卖奶，后面的拿去租
# 枚举所有情况，取最大利润（前缀和优化效率）

import sys
sys.stdin = open("rental.in", "r")
sys.stdout = open("rental.out", "w")

def by_price(item):
    return item[1]

# 根据当前i的produce，阶梯看能卖多少钱
def get_profit():
    available = produce[i]
    res = 0
    global j
    while available > 0 and j<M:
        if available >= sell[j][0]:
            res += sell[j][0]*sell[j][1]
            available -= sell[j][0]
            sell[j][0] = 0
            j += 1
        else:
            res += available*sell[j][1]
            sell[j][0] -= available
            available = 0
    return res

N,M,R = map(int, input().split())
produce = []
for i in range(N):
    milk = int(input())
    produce.append(milk)
produce.sort(reverse=True)

sell = []
for i in range(M):
    amount, price = map(int, input().split())
    sell.append([amount, price])
sell.sort(key=by_price, reverse=True)

p_sell = [0]
i = 0
j = 0

# 商店都买完后，能够自洽，不需要后置处理
while i < N:
    profit = get_profit()
    p_sell.append(p_sell[-1] + profit)
    i += 1

# read rent
rent = []
for i in range(R):
    price = int(input())
    rent.append(price)
rent.sort(reverse=True)

# 出租n头牛分别能赚多少钱
# 肯定是优先出租产奶量少的牛
p_rent = [0]
for rent_num in range(1, R+1):
    money = p_rent[-1] + rent[rent_num-1]
    p_rent.append(money)

max_money = 0
for sell_num in range(N+1):
    if N-sell_num > R:
        continue
    # 根据贪心的思想，前n头产奶量高的牛拿去卖奶，剩下的牛拿去出租
    money = p_sell[sell_num] + p_rent[N-sell_num]
    max_money = max(money, max_money)

print(max_money)


