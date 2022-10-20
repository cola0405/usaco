import sys

sys.stdin = open('breedflip.in', 'r')
sys.stdout = open('breedflip.out', 'w')

n = int(input())
A = input()
B = input()

ans = 0
i = 0
flip = False
while i < n:
    while A[i] != B[i]:
        flip = True
        i += 1
    i += 1
    if flip:
        ans += 1
        flip = False

print(ans)