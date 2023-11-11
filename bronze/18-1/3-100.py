import sys
sys.stdin = open('outofplace.in', 'r')
sys.stdout = open('outofplace.out', 'w')

n = int(input())
cows = [int(input()) for _ in range(n)]

TO_LEFT = 0
TO_RIGHT = 1
flag = TO_LEFT

# find bessie
i = 0
if cows[0] > cows[1]:
    i = 0
    flag = TO_RIGHT
elif cows[-1] < cows[-2]:
    i = n-1
    flag = TO_LEFT
else:
    for i in range(1, n-1):
        if cows[i-1]<=cows[i+1]<cows[i]:
            flag = TO_RIGHT
            break
        elif cows[i]<cows[i-1]<=cows[i+1]:
            flag = TO_LEFT
            break

# calculate op
bessie = cows[i]
s = set()
if flag == TO_RIGHT:
    i += 1
    while i<n and bessie > cows[i]:
        s.add(cows[i])
        i += 1
else:
    i -= 1
    while i>=0 and bessie < cows[i]:
        s.add(cows[i])
        i -= 1
print(len(s))