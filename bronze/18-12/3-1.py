# function的用处
# 枚举
# 很考基本功 -- set、list操作、变量控制



import sys
sys.stdin = open("backforth.in", "r")
sys.stdout = open("backforth.out", "w")

bkt1 = list(map(int, input().split()))
bkt2 = list(map(int, input().split()))

bkt1_record = tuple(bkt1)
bkt2_record = tuple(bkt2)

def move(order, r):
    inx = order[r]
    global tank1
    global tank2
    if r%2 == 0:
        src_bkt = bkt1
        dest_bkt = bkt2
        src_tank = tank1
        dest_tank = tank2
    else:
        src_bkt = bkt2
        dest_bkt = bkt1
        src_tank = tank2
        dest_tank = tank1
    if order[r] >= len(src_bkt):
        return -1
    bucket = src_bkt[inx]
    src_tank -= bucket
    dest_tank += bucket
    src_bkt.remove(bucket)
    dest_bkt.append(bucket)

    if r%2 == 0:
        tank1 = src_tank
        tank2 = dest_tank
    else:
        tank2 = src_tank
        tank1 = dest_tank


ans = set()
for a in range(11):
    for b in range(11):
        for c in range(11):
            for d in range(11):
                tank1 = 1000
                tank2 = 1000
                bkt1 = list(bkt1_record)
                bkt2 = list(bkt2_record)
                order = (a, b, c, d)

                for r in range(4):
                    res = move(order, r)
                    if res == -1:
                        break
                else:
                    res = (tank1, tank2)
                    if (tank1, tank2) not in ans:
                        ans.add(res)

print(len(ans))


