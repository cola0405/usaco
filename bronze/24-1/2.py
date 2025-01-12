# 模拟 + 优化
# 需要解决模拟结束的条件 —— 两个value为0的pad来回弹，可能导致while死循环

PAD = 0
TARGET = 1
BROKEN_TARGET = 2

n,start = map(int, input().split())

typ = [0]*(n+1)
v = [0]*(n+1)
count = [0]*(n+1)
for i in range(1,n+1):
    typ[i], v[i] = map(int, input().split())

cur = start
power,d = 1,1
ans = 0
record = set()      # 记录Bessie的运动状态
while 1 <= cur <= n:
    if typ[cur] == TARGET:
        if power >= v[cur]:
            typ[cur] = BROKEN_TARGET
            ans += 1
    elif typ[cur] == PAD:
        status = (cur, power, d)
        if status in record:        # 看当前运动状态之间是否出现过
            break
        record.add((cur, power, d))  
        d *= -1
        power += v[cur]
    cur += power*d
print(ans)
