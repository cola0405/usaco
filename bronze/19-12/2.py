import sys
sys.stdin = open('whereami.in', 'r')
sys.stdout = open('whereami.out', 'w')

n = int(input())
s = input()
for i in range(1,n+1):
    record = set()
    for j in range(n-i+1):
        seq = s[j:j+i]
        if seq in record:
            break
        record.add(seq)
    else:
        print(i)
        break