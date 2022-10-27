fin = open('speeding.in', 'r')
fout = open('speeding.out', 'w')

n, m = map(int, fin.readline().split())

speed_limit = [0]*101
speed_segments = [0]*101

i = 1
miles = 0
for _ in range(n):
    segment, limit = map(int, fin.readline().split())
    miles += segment
    while i <= miles:
        speed_limit[i] = limit
        i += 1
i = 1
miles = 0
for _ in range(m):
    segment, speed = map(int, fin.readline().split())
    miles += segment
    while i <= miles:
        speed_segments[i] = speed
        i += 1

max_diff = 0
for i in range(101):
    max_diff = max(speed_segments[i] - speed_limit[i], max_diff)

fout.write(str(max_diff))
fout.close()

