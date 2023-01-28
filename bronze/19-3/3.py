import sys
sys.stdin = open('evolution.in', 'r')
sys.stdout = open('evolution.out', 'w')


# 查看是否有特性A与特性B集合相交
def crossing(a, b):
    A, B, AB = 0, 0, 0
    for sub in subs:
        has_a, has_b = False, False
        for c in sub:
            if c == all_characteristics[a]:
                has_a = True
            if c == all_characteristics[b]:
                has_b = True
        if has_a and has_b:
            AB +=1
        elif has_a:
            A += 1
        elif has_b:
            B += 1

    return AB>0 and A>0 and B>0


n = int(input())
s = set()

# 记录每个子种群的特性及input所涉及到的所有特性
subs = []
for i in range(n):
    line = input().split()
    characteristics = line[1:]
    subs.append(characteristics)
    for c in characteristics:
        s.add(c)

all_characteristics = list(s)
num = len(all_characteristics)
ok = True

# 列举所有对，看是否存在特性A与特性B集合相交
for i in range(num):
    for j in range(i+1, num):
        if crossing(i, j):
            ok = False

if ok:
    print("yes")
else:
    print("no")



