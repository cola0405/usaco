# 信息点①
# exactly one of them has gone bad
# 只有一瓶奶出问题了
# 但注意，我们不一定能准确地把那一瓶奶找出来
# 尽可能排除，剩下地都当作有毒的

# 信息点②
# because they drank the bad milk at some strictly earlier point in time.
# 不取等号

# 排除的方法：
# 把每个生病的人喝的可能有毒的奶找出来
# 有毒的那一瓶一定在小集合里
# 则做交集来排除


PERSON = 0
TYPE = 1
TIME = 2
SICK_TIME = 1

import sys
sys.stdin = open('badmilk.in', 'r')
sys.stdout = open('badmilk.out', 'w')
n, m, d, s = map(int, input().split())


person_type_time = []
for i in range(d):
    person_type_time.append(list(map(int, input().split())))

# resume that all milk are bad, then shrink it
bad_milk = set(range(1,m+1))

for i in range(s):
    sick_people, sick_time = map(int, input().split())

    # shrink bad milk
    psb_bad_milk = set()
    for people, milk_type, time in person_type_time:
        if people == sick_people and time<sick_time:
            psb_bad_milk.add(milk_type)
    bad_milk = bad_milk.intersection(psb_bad_milk)

# count the people
possible_sick_person = set()
for person, milk_type, time in person_type_time:
    if milk_type in bad_milk:
        possible_sick_person.add(person)

print(len(possible_sick_person))





