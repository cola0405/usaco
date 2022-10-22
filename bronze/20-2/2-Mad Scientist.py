# sim
import sys

sys.stdin = open('breedflip.in', 'r')
sys.stdout = open('breedflip.out', 'w')

n = int(input())
A = input()
B = input()

ans = 0
i = 0
while i < n:
    flip = False
    while A[i] != B[i]:
        i += 1
        flip = True
    if flip:
        ans += 1
    i += 1

print(ans)