N, T = map(int, input().split())

ans = 0
# 已经吃完第 day 天的粮食
day = 0
for _ in range(N):
    di, bi = map(int, input().split())
    if ans >= T or day == T:
        break
    if di == T:
        ans += 1
        break

    if (max(di, day)+bi)-1 >= T:
        if day >= di:
            ans += T-day
        else:
            ans += (T-di) + 1
        day = T
        break
    # 没超的都能吃
    else:
        #if di+bi-1 <= day:
        if di <= day:
            day += bi
        else:
            # day += bi-1
            day = di+bi-1
        ans += bi

if ans >= T:
    print(T)
else:
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