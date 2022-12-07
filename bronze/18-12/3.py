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

nums = [0,1,2,3,4,5,6,7,8,9,10]

def move(inx, src_tank, dest_tank, src_bkt, dest_bkt):
    if inx >= len(src_bkt):
        return -1
    bucket = src_bkt[inx]
    src_tank -= bucket
    dest_tank += bucket
    src_bkt.remove(bucket)
    dest_bkt.append(bucket)
    return src_tank, dest_tank


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

                for inx in [0,2]:
                    res = move(order[inx], tank1, tank2, bkt1, bkt2)
                    if res == -1:
                        continue
                    else:
                        tank1, tank2 = res
                    res = move(order[inx+1], tank2, tank1, bkt2, bkt1)
                    if res == -1:
                        continue
                    else:
                        tank2, tank1 = res
                else:
                    res = (tank1, tank2)
                    if res not in ans:
                        ans.add(res)

print(len(ans))


