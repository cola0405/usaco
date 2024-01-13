# 用dict减少冗余的if判断

T = int(input())
for u in range(T):
    n, k = map(int, input().split())
    cows = input()

    cur = {'G': -float('inf'), 'H': -float('inf')}
    ans = ['.']*n
    count = 0
    for i in range(n):
        if abs(i-cur[cows[i]]) > k:
            right = min(i+k, n-1)
            while ans[right] != '.':
                right -= 1
            cur[cows[i]] = right
            ans[right] = cows[i]
            count += 1

    print(count)
    print(''.join(ans))

