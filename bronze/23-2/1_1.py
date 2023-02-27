N, T = map(int, input().split())

ans = 0
# 已经吃完第 day 天的粮食
money = 0
last_day = 0
ans = 0
for _ in range(N):
    di, bi = map(int, input().split())
    if _ == 0:
        last_day = di
        money += bi
        continue

    money += bi
    gap = di - last_day

    if money >= gap:
        ans += gap
        money -= gap
    else:
        ans += money
        money = 0

if money >= gap:
    ans += gap
    money -= gap
else:
    ans += money
    money = 0

print(ans)




# 2 5
# 3 5
# 4 5
 # 3

# 2 5
# 3 3
# 4 4
 # 3



# 3 5
# 3 2
# 4 1
# 5 1
 # 3


# 2 5
# 3 2
# 4 2
 # 3

# 2 10
# 3 5
# 4 4

# 2 10
# 3 5
# 5 5
 # 8

# 3 10
# 1 5
# 6 3
# 9 1
 # 9

# 3 10
# 1 1
# 3 3
# 4 6