'''
动态维护 counter

从左往右走
统计 count>2的数字的个数

就是要注意避免重复计算
'''


from collections import Counter
n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
cnt2 = 0        # 统计cnt中2以上的个数
for i in cnt:
    if cnt[i] >= 2:
        cnt2 += 1

vis = [0]*(n+1)     # 已经开头过的数字不再开头
ans = 0
for i in range(n):
    cnt[a[i]] -= 1
    if cnt[a[i]] == 1:
        cnt2 -= 1
    if vis[a[i]]: continue
    ans += cnt2
    vis[a[i]] = 1
    if cnt[a[i]] >= 2:  # 除去开头的数字本身
        ans -= 1
print(ans)


'''
6
1 2 3 4 4 4

'''