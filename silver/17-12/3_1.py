# A shuffle is described with N numbers, where a cow in position i moves to position ai
# 就是说，每次只移动一只奶牛！
# after which they will move together for all remaining shuffles.
# 上面这句话的意思是，在接下来的大调换，是在当前的状态的基础上进行！
import sys
sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

n = int(input())
dest = [0]+list(map(int, input().split()))

flag = [0]*(n+1)
for i in range(1,n+1):
    if flag[i] == 1 or flag[i] == -1:
        continue
    cur = i
    already = {i}
    for j in range(n):
        pre = cur  # 前后指针
        cur = dest[cur]
        if flag[cur] == 1 or flag[cur] == -1:
            break
        if cur in already:
            flag[pre] = 1
            flag[cur] = 1
            p = dest[cur]
            while flag[p] == 0:  # fill the cycle
                flag[p] = 1
                p = dest[p]
            break
        already.add(cur)

    # for invalid chain, abandon useless items
    for item in already:
        if flag[item] == 0:
            flag[item] = -1
print(flag.count(1))
