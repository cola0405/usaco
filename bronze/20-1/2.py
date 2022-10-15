import sys

sys.stdin = open('photo.in', 'r')
sys.stdout = open('photo.out', 'w')

n = int(input())
b = list(map(int, input().split()))


for i in range(1, n+1):
    j = 0
    ans = [b[j]]
    temp_a = b[j] - i
    if temp_a < 0:
        continue
    ans.append(str(temp_a))
    while temp_a > 0 and j < len(b):
        temp_a = b[j] - temp_a
        j += 1
    if j == len(b):
        print(''.join(ans))

