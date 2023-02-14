# 近似法

n = int(input())

locs = set()
says = []
for i in range(n):
    line = input().split()
    word = line[0]
    loc = int(line[1])
    locs.add(loc)
    says.append((word, loc))

ans = 1000
for loc in locs:
    liar = 0
    for say in says:
        # 条件一点都不能改
        if say[0] == 'G' and loc < say[1]:
            liar += 1
        elif say[0] == 'L' and loc > say[1]:
            liar += 1
    ans = min(ans, liar)

print(ans)
