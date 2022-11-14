
# 不注意的话错8个测试用例（总共17个）
# 它可以先引用mid呀！

# 6 10
# 2 2 3 3 3 3
# 应该输出：4
# 如果按照当前算法，输出的是3，因为他只往左看


n, L = map(int, input().split())
cites = list(map(int, input().split()))
cites.sort()


def get_one_diff_num(i):
    c = cites[i]
    i -= 1
    count = 0
    while i >= 0 and count < L:
        if cites[i]+1 == c:
            count += 1
        i -= 1
    return count

def get_same_sites_on_left(i):
    c = cites[i]
    i -= 1
    count = 0
    # 因为它自己也引用，所以这里用L-1
    # 影响到一个测试用例
    while i >= 0 and count < L-1:
        if cites[i] == c:
            count += 1
        i -= 1
    return count


left = 0
right = n-1
ans = 0
while left <= right:
    mid = (left+right)//2

    # 容易忽略的一点是，它可以先引用当前mid的，提升一个档次
    # 差1的是可以通过L提上来的
    # 注意到了这一点，又对了两个此时用例
    num1 = get_one_diff_num(mid)
    num2 = get_same_sites_on_left(mid)
    if n-mid+num1 >= cites[mid]:
        ans = max(ans, cites[mid])
        left = mid+1
    else:
        right = mid-1
    if num2+1 >= cites[mid]+1:
        ans = max(ans, cites[mid]+1)

print(ans)



