n,q = map(int, input().split())
close = list(map(int, input().split()))
t = list(map(int, input().split()))
gap = [close[i]-t[i] for i in range(n)]
gap.sort()

for r in range(q):
    v,s = map(int, input().split())
    low = 0
    high = n-1
    while low < high:
        mid = (low+high)//2
        if gap[mid] > s:
            high = mid
        else:
            low = mid+1
    if gap[low] > s and n-low >= v:
        print('YES')
    else:
        print('NO')

