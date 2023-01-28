# 几何overlap
# 右边取min(b,d)，左边取max(a,c)
# 再和0作比较

import sys
sys.stdin = open('paint.in', 'r')
sys.stdout = open('paint.out', 'w')

a, b = map(int, input().split())
c, d = map(int, input().split())

overlap = max(0, min(b,d) - max(a,c))
ans = (b-a)+(d-c) - overlap
print(ans)