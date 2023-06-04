# 画图找规律一下就出来了
# 1e18 肯定是二分处理
import sys
sys.stdin = open("cowcode.in", "r")
sys.stdout = open("cowcode.out", "w")

s, n = input().split()
n = int(n)

k = len(s)
while k*2<n:
    k *= 2

while n > len(s):
    if k+1 != n:
        n -= k + 1
    else:
        n = k  # “cowwcoo” oo处理不太一样
    while k >= n:
        k //= 2
print(s[n-1])