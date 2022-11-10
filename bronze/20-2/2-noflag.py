import sys
sys.stdin = open('breedflip.in', 'r')
sys.stdout = open('breedflip.out', 'w')


n = int(input())
A = input()
B= input()

i = 0
ans = 0
while i < n:
    if A[i] == B[i]:
        i += 1
        continue
    while i < n and A[i] != B[i]:
        i += 1
    ans += 1
print(ans)