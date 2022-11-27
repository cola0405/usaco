fin = open('herding.in', 'r')
fout = open('herding.out', 'w')
lst = list(map(int, fin.readline().strip().split()))
mins = min(lst[1] - lst[0], lst[2]-lst[1])
maxs = max(lst[1] - lst[0], lst[2]-lst[1])
if mins == maxs == 1:
    fout.write('0')
    fout.write('\n')
    fout.write('0')
elif mins == 1 and maxs == 2:
    fout.write('1')
    fout.write('\n')
    fout.write('1')
elif mins == 1 and maxs > 2:
    fout.write('2')
    fout.write('\n')
    fout.write(str(maxs-1))
elif mins == maxs == 2:
    fout.write('1')
    fout.write('\n')
    fout.write('1')
elif mins == 2 and maxs > 2:
    fout.write('1')
    fout.write('\n')
    fout.write(str(maxs-1))
else:
    fout.write('2')
    fout.write('\n')
    fout.write(str(maxs-1))