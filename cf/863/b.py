# https://codeforces.com/contest/863/

n = int(input())
w = list(map(int, input().split()))
w.sort()

ans = float('inf')
for i in range(2*n):
    for j in range(i+1,2*n):
        the_w = w[:]
        the_w.pop(i)
        the_w.pop(j-1)

        gap = 0
        for k in range(0, len(the_w)-1, 2):
            gap += the_w[k+1] - the_w[k]
        ans = min(gap, ans)
print(ans)




