n,m = map(int, input().split())
cow = list(map(int, input().split()))
candies = list(map(int, input().split()))

for candy in candies:
    bottom = 0
    for i in range(n):
        if cow[i] >= bottom:
            gap = min(candy-bottom, cow[i]-bottom)    # 糖还有剩或被吃完
            cow[i] += gap
            bottom += gap

        if bottom == candy:     # bottom 到顶 —— 糖果吃完了
            break

for height in cow:
    print(height)
