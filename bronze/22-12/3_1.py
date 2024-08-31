# analyse + topologic

# 题意:
# 题目给定一些输入和对应的输出，问是否存在那么一段if判断程序，可以处理这些输入、输出

# 因为 if 的条件只有一个，所以对于每一个输入
# 我们需要找到一个独特的位，可以让我们把它单独筛出来
# 如果暂时还找不到，那就先放着，等某些冲突的输入已经被前面的if筛出去之后再搜索独特位
# 这就是拓扑的策略

from collections import deque

t = int(input())
for _ in range(t):
    input()
    n, m = map(int, input().split())
    dq = deque()
    for r in range(m):
        s, res = input().split()
        dq.append([s, res])

    cnt = len(dq)
    while dq and cnt:
        s0, res0 = dq.popleft()
        conflict = True
        for i in range(n):  # 第i位做判断
            for s1, res1 in dq:  # 遍历整个dq，看是否存在矛盾
                if s1[i]==s0[i] and res1!=res0:
                    break
            else:
                conflict = False
                cnt = len(dq)  # cnt防止无限循环
                break
        if conflict:           # 如果找到独特位，那就表示可以单独筛走，不需要再放入dq
            dq.append([s0, res0])
            cnt -= 1

    if len(dq)==0:
        print("OK")
    else:
        print("LIE")


