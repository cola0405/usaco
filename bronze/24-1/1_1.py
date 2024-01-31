from collections import Counter
t = int(input())
for r in range(t):
    n = int(input())
    cows = list(map(int, input().split()))
    ans = set()
    for i in range(n-2):
        count = Counter(cows[i:i+3])
        for cow in count:
            if count[cow] >= 2:     # 只要有1+2 则可不断蚕食
                ans.add(cow)

    ans = sorted(ans)
    if len(ans) == 0:
        if len(set(cows)) == 1:
            print(cows[0])
        else:
            print(-1)
    else:
        print(' '.join(map(str, ans)))



