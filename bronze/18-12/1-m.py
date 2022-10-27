fin = open('mixmilk.in', 'r')
fout = open('mixmilk.out', 'w')

B1_TO_B2 = 0
B2_TO_B3 = 1
B3_TO_B1 = 2


def pour(flag):
    src = flag
    des = (flag+1)%3
    if m[src] + m[des] > c[des]:
        m[src] = (m[src]+m[des]) - c[des]
        m[des] = c[des]
    else:
        m[des] += m[src]
        m[src] = 0
    return m[0], m[1], m[2], des


# input
m = [0]*3
c = [0]*3
for i in range(3):
    c[i], m[i] = map(int, fin.readline().split())

# simulation
round = 1
status = None
while round <= 100:
    status = pour(B1_TO_B2)
    round += 1

for i in status[:3]:
    fout.write(str(i)+"\n")
fout.close()

