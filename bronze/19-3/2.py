# 题目规则下的特点
# 最终要找的all to one，是不允许作为起始点的
# 你可能会想，没办法直接到达，那可以通过其他站点到达
# 但是别忘了，只有n-1条传送带
# 如果要构成回路，那么肯定不止n-1条传送带，好好理解图的这个特点

import sys
sys.stdin = open('factory.in', 'r')
sys.stdout = open('factory.out', 'w')

n = int(input())
ways = set()
for i in range(1, n+1):
    ways.add(i)

for i in range(n-1):
    source, dest = map(int, input().split())
    if source in ways:
        ways.remove(source)

if len(ways) == 1:
    for i in ways:
        print(i)
else:
    print(-1)
