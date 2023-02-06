# n2 只能过3个测试用例
n = int(input())
h = list(map(int, input().split()))

ans = 0
m_stack = []

for i in range(n):
    # 把栈内比新h[i]矮得都pop出去，因为他们都是小于min(hi,hj)的
    # pop的同时计算可扔飞盘的距离
    while len(m_stack)>0 and h[m_stack[-1]] < h[i]:
        gap = i-m_stack[-1]+1
        ans += gap
        m_stack.pop()
    # i+1后 栈仍然单调，则说明又可以更新ans
    if len(m_stack)>0:
        gap = i-m_stack[-1]+1
        ans += gap
    m_stack.append(i)

print(ans)


