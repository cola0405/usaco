# 贪心
# 筛掉一些后，可能会有新的转机
# 又从头看

# 不用担心筛的顺序
# 因为能筛的那部分就是能筛的，先后顺序不影响
#（筛掉之后只会使原来不可以的变为可以，并不会使原来可以的变得不可以）

t = int(input())

def is_consistent(col, inp):
    outps = set()
    for row in range(len(program)):
        program_inp = program[row][0]
        if program_inp[col] == inp:
            program_outp = program[row][1]
            outps.add(program_outp)
    return len(outps) == 1

for _ in range(t):
    input()
    n,m = map(int, input().split())
    program = []
    for i in range(m):
        program.append(input().split())
    while len(program) > 0:
        for col in range(n):
            # inp='0'时，对应的res是否都一致
            if is_consistent(col, inp='0'):
                # filter 留True
                # 筛去0的，留下非0的
                program = list(filter(lambda p:p[0][col] != '0', program))
                break
            if is_consistent(col, inp='1'):
                program = list(filter(lambda p:p[0][col] != '1', program))
                break
        else:
            print('LIE')
            break
    else:
        print('OK')

