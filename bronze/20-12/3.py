

record_dict = {'N':[], 'E':[], 'S':[], 'W':[]}
records = []

n = int(input())
for i in range(n):
    direction, x, y = input().split()
    record_dict[direction].append((int(x), int(y)))
    records.append((direction, int(x), int(y)))

already_check = [0]*n


for i in range(n):
    direction1 = records[i][0]
    point1 = records[i][1:]
    for j in range(n):
        if j == i:
            continue
        direction2 = records[j][0]
        point2 = records[j][1:]


        # interact or not
        if direction1 == direction2:
            continue
        ix,iy = point1
        jx,jy = point2
        x_gap = abs(ix - jx)
        y_gap = abs(iy - jy)
        # 拦不到
        if direction1 == 'E' and direction2 == 'N' \
            and x_gap - y_gap >= 1:
            continue
        # 拦到了记录，则记录gap，最后取最大
        # 如果gap为-1，则是没人能拦到
        for k in range(n):
            if k == i or k == j:
                continue
            direction3 = records[k][0]
            point3 = records[k][1:]

            # whether interrupt
            if direction3 == direction2:
                pass
        # if valid then count it
    # get the max




