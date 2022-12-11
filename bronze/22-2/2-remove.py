# 11/14
n = int(input())
origin = list(map(int, input().split()))
goal = list(map(int, input().split()))

ans = 0
i = 0
j = 0
while i < len(origin) and j < n:
    if origin[i] != goal[j]:
        ans += 1
        origin.remove(goal[j])
    else:
        i += 1
    j += 1

print(ans)