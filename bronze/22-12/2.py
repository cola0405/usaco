# 贪心
# 尽可能把草地往右边种 -- 如此一来左边顾到了，右边也能尽可能覆盖多的cow

T = int(input())
for u in range(T):
    n, k = map(int, input().split())
    cows = input()

    last = {'G': -float('inf'), 'H': -float('inf')}   # 记录上一个草的位置
    ans = ['.']*n
    count = 0
    for i in range(n):
        if abs(i-last[cows[i]]) > k:        # 如果吃不到上一个草，那就得往右边新种
            right = min(i+k, n-1)
            while ans[right] != '.':        # 如果right处已经被种了，那就往左边找空位
                right -= 1
            last[cows[i]] = right
            ans[right] = cows[i]
            count += 1

    print(count)
    print(''.join(ans))

