from collections import defaultdict

def check():
    low = 0
    high = float('inf')
    for i in range(n):
        idx1 = taller_idx[i]
        height1 = plants[idx1]
        speed1 = speeds[idx1]

        for j in range(i+1, n):
            idx2 = taller_idx[j]
            height2 = plants[idx2]
            speed2 = speeds[idx2]

            gap = speed1 - speed2
            if height1 == height2:
                if gap <= 0:
                    print(-1)
                    return
            elif height1 > height2:
                if gap < 0:
                    high = min(high, (height1-height2) // abs(gap))
            else:
                if gap <= 0:
                    print(-1)
                    return
                low = max(low, (height2-height1) // abs(gap) + 1)

            if low > high:
                print(-1)
                return
    print(low)

T = int(input())
for r in range(T):
    n = int(input())
    plants = list(map(int, input().split()))
    speeds = list(map(int, input().split()))
    taller = list(map(int, input().split()))

    plants_idx = defaultdict(int)
    speeds_idx = defaultdict(int)
    taller_idx = defaultdict(int)

    for i in range(n):
        plants_idx[plants[i]] = i
        speeds_idx[speeds[i]] = i
        taller_idx[taller[i]] = i

    sorted_plants = sorted(plants, reverse=True)
    sorted_speeds = sorted(speeds, reverse=True)
    sorted_taller = sorted(taller)

    check()

