import sys
sys.stdin = open("swap.in", "r")
sys.stdout = open("swap.out", "w")

n,m,k = map(int, input().split())
order = [tuple(map(int, input().split())) for _ in range(m)]

cows = list(range(1,n+1))
record = [tuple(cows)]
for i in range(k):
    for a,b in order:
        cows[a-1:b] = cows[a-1:b][::-1]
    cur_cows = tuple(cows)
    if cur_cows not in record:
        record.append(tuple(cows))
    else:
        for cow in record[k%len(record)]:
            print(cow)
        exit()
for cow in record[-1]:
    print(cow)