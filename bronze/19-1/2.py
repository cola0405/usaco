fin = open("sleepy.in", "r")
fout = open("sleepy.out", "w")

n = int(fin.readline())
cows = list(map(int, fin.readline().split()))

ans = 0
i = len(cows)-1
while i > 0:
    if cows[i] < cows[i-1]:
        ans = i
        break
    i -= 1

fout.write(str(ans))
fout.close()



