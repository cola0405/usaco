# min 只有三种情况 0 1 2
# max 就是 max_gap
import sys
sys.stdin = open('herding.in', 'r')
sys.stdout = open('herding.out', 'w')

a,b,c = sorted(map(int, input().split()))

min_gap = min(b-a, c-b)-1
max_gap = max(b-a, c-b)-1

if max_gap == 0:
    print(0)
elif min_gap == 1:
    print(1)
else:
    print(2)
print(max_gap)

