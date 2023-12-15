T = int(input())
for r in range(T):
    n = int(input())
    plants = list(map(int, input().split()))
    speeds = list(map(int, input().split()))
    taller = list(map(int, input().split()))
    taller_idx = {taller[i]: i for i in range(n)}

    low = 0
    high = float('inf')
    for x in range(n-1):
        for i in range(n-1):
            idx1 = taller_idx[i]
            height1 = plants[idx1]
            speed1 = speeds[idx1]

            idx2 = taller_idx[i+1]
            height2 = plants[idx2]
            speed2 = speeds[idx2]

            if speed1 > speed2:
                low = max(low, (height2-height1)//(speed1-speed2)+1)
            elif speed1 == speed2:
                if height1 <= height2:
                    low = -1
                    break
            else:
                if height1 <= height2:
                    low = -1
                    break
                high = min(high, (height1-height2)//(speed2-speed1))
    print(low)

