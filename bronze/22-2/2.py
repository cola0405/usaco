# set 完美解决remove耗时的问题


n = int(input())
origin = list(map(int, input().split()))
goal = list(map(int, input().split()))

ans = 0
i = 0
j = 0
abandon = set()
while i < len(origin) and j < n:
    if origin[i] in abandon:
        i += 1
        continue
    if origin[i] != goal[j]:
        ans += 1
        abandon.add(goal[j])
    else:
        i += 1
    j += 1
print(ans)