import sys
sys.stdin = open('photo.in', 'r')
sys.stdout = open('photo.out', 'w')

n = int(input())
b = list(map(int, input().split()))

for x in range(1, n + 1):               # try every possible a1
    ans = [x]
    for bi in b:
        x = bi - x                      
        if x <= 0 or x in ans:          # number should between 1 and n
            break                       # number should not be repeated
        ans.append(x)
    else:
        print(' '.join(map(str, ans)))
        break
