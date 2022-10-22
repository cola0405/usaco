# 是否取等号 -- 重要检查项

import sys

sys.stdin = open('photo.in', 'r')
sys.stdout = open('photo.out', 'w')

n = int(input())
b = list(map(int, input().split()))

for current_a in range(1, n + 1):
    ans = [str(current_a)]
    for bi in b:
        current_a = bi - current_a

        # number should between 1 and n
        if current_a <= 0:
            break

        # number should not be repeated
        if str(current_a) not in ans:
            ans.append(str(current_a))
        else:
            break
    else:
        print(' '.join(ans))
        break
