# 2D geometry
# 熟练运用交集的几何知识

# consider of this situation
#    ******
#    *    *
# *************
# *  *    *   *
# *************
#    *    *
#    ******

import sys
sys.stdin = open('billboard.in', 'r')
sys.stdout = open('billboard.out', 'w')
ax,ay,bx,by = map(int, input().split())
cx,cy,dx,dy = map(int, input().split())

min_top = min(by,dy)
min_right = min(bx, dx)
max_bottom = max(ay,cy)
max_left = max(ax,cx)
ans = (by-ay) * (bx-ax)

# cover 2 edges
if (min_top == by or max_bottom == ay) and (min_right == bx or max_left == ax):
    h = min_top - max_bottom
    w = min_right - max_left
    if h == by-ay or w == bx-ax:    # all cover
        ans -= w*h
print(ans)
