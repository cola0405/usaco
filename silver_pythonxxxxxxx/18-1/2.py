# 贪心策略是 -- 肯定产奶量高的奶牛拿去卖奶，低的拿去租
# 排序，然后前n头牛拿去卖奶，后面的拿去租
# 枚举所有情况，取最大利润（前缀和优化效率）

import sys
sys.stdin = open("rental.in", "r")
sys.stdout = open("rental.out", "w")


N,M,R = map(int, input().split())

# read produce
produce = []
for i in range(N):
    milk = int(input())
    produce.append(milk)
produce.sort(reverse=True)

# read sell
sell = []
for i in range(M):
    amount, price = map(int, input().split())
    sell.append((amount, price))

def by_price(item):
    return item[1]
sell.sort(key=by_price, reverse=True)

# 根据produce，阶梯看能卖多少钱
def milks_money(total):
    money = 0
    i = 0
    while total > 0:
        if total - sell[i][0] > 0:
            money += sell[i][0] * sell[i][1]
            i += 1
        else:
            money += total * sell[i][1]
        total -= sell[i][0]
    return money




# build prefix sum of selling
# 贪心法+双指针，看前n头牛的奶能卖多少钱
p_sell = [0]
i = 0
j = 0
remain = sell[j][0]
price = sell[j][1]
while i < N and j < M:
    money = 0
    milk = produce[i]
    while milk > 0 and j < M:
        if milk > remain:
            milk -= remain
            money += remain * price
            j += 1
            if j == M:
                break
            remain = sell[j][0]
            price = sell[j][1]
        else:
            money += milk * price
            remain -= milk
            milk = 0
    p_sell.append(p_sell[-1] + money)
    i += 1
# 后置处理
while i < N:
    p_sell.append(p_sell[-1])
    i += 1

# read rent
rent = []
for i in range(R):
    price = int(input())
    rent.append(price)
rent.sort(reverse=True)

# build prefix sum of renting
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


