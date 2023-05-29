# not done
import heapq
import sys
sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

class Cow():
    def __init__(self, id, val):
        self.id = id
        self.val = val

    def __repr__(self):
        return '{}:{}'.format(self.id,self.val)

    def __lt__(self, other):
        return self.val < other.val


n,g = map(int, input().split())
records = []
for _ in range(n):
    day, ID, val = map(int, input().split())
    records.append((day,ID,val))

records.sort(key=lambda item: item[0])

heap = [Cow(-1, -g)]
already = {-1,}
cows = {-1: heap[0]}
cur = set()  # ids on display, can't use this, because there are too much
ans = 0
for record in records:
    other = 0
    ID, val = record[1], record[2]
    pre_head = heap[0]
    pre_val = heap[0].val
    if ID in already:
        cows[ID].val -= val
        if ID != heap[0].id:
            other = 1
        heapq.heapify(heap)

    else:
        other = 1
        already.add(ID)
        cow = Cow(ID, -g-val)
        heapq.heappush(heap, cow)
        cows[ID] = cow

    # max 12降为11时 不应该修改的
    if heap[0].val != pre_val or (other == 1 and cows[ID].val):
        ans += 1

print(ans)

"""
4 10
1 1 +2
2 2 -2
3 1 -1
4 2 +3
"""
