# pass the ball to the cow farthest to the left among these
# 把球传给最靠左的那头牛

# 1.孤独的牛--init 给
# 2.“只给对方”--给（有第三方给进来都不算）

import sys
sys.stdin = open("hoofball.in","r")
sys.stdout = open("hoofball.out","w")

n = int(input())
x = list(map(int, input().split()))
x.sort()

def target(i):
    if i == 0:
        return 1
    if i == n-1:
        return n-2
    left = x[i-1]
    right = x[i+1]
    if x[i] - left <= right - x[i]:
        return i-1
    else:
        return i+1

passto = [0]*n
for i in range(n):
    passto[target(i)] += 1

ans = 0
for i in range(n):
    if passto[i] == 0:
        ans += 1
    # ps: passto都是计数为1,才算是“只给对方”，好好理解
    # ps: i<target(i) 来保证不重复计数
    elif i < target(i) and target(target(i)) == i \
            and passto[i] == 1 and passto[target(i)] == 1:
        ans += 1

print(ans)
