fin = open('square.in', 'r')
fout = open('square.out', 'w')

line1 = fin.readline()
line2 = fin.readline()
ax1, ay1, ax2, ay2 = map(int, line1.split())
bx1, by1, bx2, by2 = map(int, line2.split())
fin.close()

x1 = min(ax1, bx1)
y1 = min(ay1, by1)

x2 = max(ax2, bx2)
y2 = max(ay2, by2)

area = max((x2-x1),(y2-y1))**2

fout.write(str(area))
fout.close()

