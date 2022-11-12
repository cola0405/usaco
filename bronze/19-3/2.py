# 题目规则下的特点
# input确定是一个连通的图
# 看题目开头，John为了节约成本，用n-1个通道连接了所有的station
# 只是没有考虑到传送带是单向的

# 最终要找的all to one，是不允许作为起始点的
# 你可能会想，没办法直接到达，那可以通过其他站点到达
# 但是别忘了，只有n-1条传送带
# 如果要构成回路，那么肯定不止n-1条传送带，好好理解图的这个特点


# 再就是证明为什么只剩下一个的时候，那个点就是点i
# 一步一步推
# 剩下的一个点x没有作起始点，但又要构成连通，则必定有一个y点到x
# 那么对于当前的两个点，如果还要与其他点连通
# 只有三个选择，y到z、z到x、z到y（有前提条件的，x是剩下的那一个点）
# 如果是y到z，那么z也是不作为起始点，与已知条件相悖（只剩下x不做起始点）
# 如果是z到x，那么可以呀，但此时i仍然可以是station i
# 如果是z到y，同上
# 再有新的点以此类推即可

# 总结一下， 就是说，在“连通 + 只剩一个station + n-1条通道”的前提下
# 剩下的那一个station就是目标

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
