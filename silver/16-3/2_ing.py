import sys
sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")

n,k = map(int, input().split())
diamonds = [int(input()) for _ in range(n)]
diamonds.sort()

l = 0
r = 0
ans = 0
while l<=r<len(diamonds):
    if diamonds[r]-diamonds[l] <= k:
        ans = max(r-l + 1, ans)
        r += 1
    else:
        l += 1
print(ans)