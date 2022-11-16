# 利用周期压缩k
# 同时注意不到一个周期的处理

# tuple 可hash，list不可hash
# 切片的坑[1:-1:-1]会输出空的数组


import sys
sys.stdin = open('swap.in', 'r')
sys.stdout = open('swap.out', 'w')

n, k = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
a1 -= 1
a2 -= 1
b1 -= 1
b2 -= 1

prev = list(range(1,n+1))
prev_record = tuple(prev)
record = [prev_record]
record_set = {prev_record}

for i in range(k):
    # first step
    if a1 == 0:
        prev[a1:a2 + 1] = prev[a2::-1]
    else:
        prev[a1:a2+1] = prev[a2:a1-1:-1]

    # second step
    if b1 == 0:
        prev[b1:b2 + 1] = prev[b2::-1]
    else:
        prev[b1:b2+1] = prev[b2:b1-1:-1]

    current = tuple(prev)
    if current not in record_set:
        record_set.add(current)
        record.append(current)
    else:
        cycle = len(record_set)
        ans = record[k%cycle]
        break
else:
    ans = record[-1]

for i in ans:
    print(i)



