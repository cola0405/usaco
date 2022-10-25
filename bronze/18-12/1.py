B1_TO_B2 = 1
B2_TO_B3 = 2
B3_TO_B1 = 0

def pour(m1, m2 ,m3, flag):
    if flag == B1_TO_B2:
        if m1+m2 > c2:
            m1 = (m1+m2) - c2
            m2 = c2
        else:
            m2 += m1
            m1 = 0
    elif flag == B2_TO_B3:
        if m2+m3 > c3:
            m2 = (m2+m3) - c3
            m3 = c3
        else:
            m3 += m2
            m2 = 0
    elif flag == B3_TO_B1:
        if m3+m1 > c1:
            m3 = (m3+m1) - c1
            m1 = c1
        else:
            m1 += m3
            m3 = 0
    return m1, m2, m3, (flag+1)%3

fin = open('mixmilk.in', 'r')
fout = open('mixmilk.out', 'w')


c1, m1 = map(int, fin.readline().split())
c2, m2 = map(int, fin.readline().split())
c3, m3 = map(int, fin.readline().split())

record = []

round = 1
ans = -1
ans_index = -1
status = (m1, m2, m3, B1_TO_B2)
while round <= 100:
    if status not in record:
        record.append(status)
    else:
        index = record.index(status)
        cycle_len = round - index - 1
        ans_index = (100-index) % cycle_len
        record = record[index:round]
        break
    status = pour(status[0], status[1], status[2], status[3])
    round += 1


if ans_index == -1:
    status = record[-1]
    for i in status[:3]:
        fout.write(str(i) + "\n")
else:
    status = record[ans_index]
    for i in status[:3]:
        fout.write(str(i)+"\n")
fout.close()

