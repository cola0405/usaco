# 启蒙用例
# HHHHGHH
# 跟相邻的异种数量有关！
# 每头牛都是研究对象，看其左右

n = int(input())
s = input()

left = []
right = []
ans = 0

for i in range(n):
    # left
    count = 0
    index = i-1
    while index >= 0:
        if s[index] != s[i]:
            count += 1
        else:
            break
        index -= 1
    left.append(count)

    # right
    count = 0
    index = i + 1
    while index < n:
        if s[index] != s[i]:
            count += 1
        else:
            break
        index += 1
    right.append(count)

    ans += max(left[i]-1, 0)
    ans += max(right[i]-1, 0)
    ans += left[i]*right[i]

print(ans)
