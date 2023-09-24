import sys
sys.stdin = open("citystate.in", "r")
sys.stdout = open("citystate.out", "w")

n = int(input())

d = dict()
records = []
for i in range(n):
    name, code = input().split()
    records.append((name, code))

    head = name[:2]
    s = head+code
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1


ans = 0
for name, code in records:
    head = name[:2]
    if head == code:
        continue
    s = code+head
    # 每一对都可以组的
    if s in d:
        ans += d[s]
print(ans//2)
