# 近似法

n = int(input())

nums = set()
says = []
for i in range(n):
    line = input().split()
    word = line[0]
    num = int(line[1])
    nums.add(num)
    says.append((word, num))

ans = 1000
for num in nums:
    liar = 0
    for say in says:
        if say[0] == 'G':
            if num < say[1]:
                liar += 1
        else:
            if num > say[1]:
                liar += 1
    ans = min(ans, liar)

print(ans)
