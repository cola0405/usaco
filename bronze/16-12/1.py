# geometry

import sys
sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")

line1 = input()
line2 = input()
ax1, ay1, ax2, ay2 = map(int, line1.split())
bx1, by1, bx2, by2 = map(int, line2.split())

x1 = min(ax1, bx1)
y1 = min(ay1, by1)

x2 = max(ax2, bx2)
y2 = max(ay2, by2)

area = max((x2-x1),(y2-y1))**2

print(area)

