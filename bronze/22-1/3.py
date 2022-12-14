# 找到final line 这题就结束了

# 保持每队i和i+1一致的前提下，不断贪心去压
# 一旦发现无法维持i和i+1一致，则输出-1

round = int(input())
ans = 0
for r in range(round):
    n = int(input())
    levels = list(map(int, input().split()))
    record = tuple(levels)
    i = 0
    while i < n-1:
        if levels[i] < 0:
            break
        if levels[i] > levels[i+1]:
            # i%2==0 说明i项前刚好有n对
            # 又i项>i+1项，说明i和i-1项需要减了
            # 但是如果i-1正好是一对中的right
            # 那么就打破了一对的平衡，也就意味着g了，输出-1
            if i%2 == 0:
                break
            levels[i] = levels[i+1]
        elif levels[i] < levels[i+1]:
            # i+1项大， 就需要i+2压下来
            # 如果没有i+2，则意味着压不了，也g了，输出-1
            if i+2 >= n:
                break
            diff = levels[i+1] - levels[i]
            levels[i+2] -= diff
            levels[i+1] = levels[i]
            if levels[i+2] < 0:
                break
        i += 1
    else:
        # find the final line
        v = levels[n - 1]
        ans = 0
        for level in record:
            ans += level - v
        print(ans)
        continue
    print(-1)






