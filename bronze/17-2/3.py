import sys
sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

n = int(input())
record = []
for i in range(n):
    start, gap = map(int, input().split())
    record.append((start,gap))

def by_time(r):
    return r[0]
record.sort(key=by_time)

cur_time = 0
for i in range(n):
    start, gap = record[i]
    if start > cur_time:
        cur_time = start
    cur_time += gap

print(cur_time)

