import sys
sys.stdin = open('photo.in', 'r')
sys.stdout = open('photo.out', 'w')


n = int(input())
B = list(map(int, input().split()))
A = []
for a in range(1, n+1):
    i = 0
    A = [a]
    for b in B:
        a_next = b - a
        # number should between 1 and n
        # number should not be repeated
        if a_next <= 0 or a_next in A:
            break
        A.append(a_next)
        a = a_next
    else:
        break

A = list(map(str, A))
print(' '.join(A))