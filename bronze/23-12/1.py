n,m = map(int, input().split())
cow = list(map(int, input().split()))
candies = list(map(int, input().split()))

for candy in candies:
    low = 0
    for i in range(n):
        if cow[i] >= low:
            gap = min(candy-low, cow[i]-low)
            cow[i] += gap
            low += gap

        if low >= candy:
            break

for height in cow:
    print(height)
