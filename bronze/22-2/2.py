# two pointers
# use Set to optimize the remove operation

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
s = set()
for j in range(n):       # j is the index for b
    while a[i] in s:     # check a[i] is removed or not
        i += 1  
    if a[i] == b[j]:
        i += 1
    else:
        s.add(b[j])
print(len(s))