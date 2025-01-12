# math
# 只考虑相邻的3个元素即可
# 只要有1+2 则可不断蚕食
# 1 1 2 或者 1 2 1  -- 相邻、或者夹住

from collections import Counter
t = int(input())
for r in range(t):
    n = int(input())
    cows = list(map(int, input().split()))
    if len(set(cows)) == 1:
        print(cows[0])
        continue
    ans = set()
    for i in range(n-2):
        count = Counter(cows[i:i+3])
        for cow in count:
            if count[cow] >= 2:     # 只要有1+2 则可不断蚕食
                ans.add(cow)
    if len(ans) == 0: print(-1)
    else: print(' '.join(map(str, sorted(ans))))
    