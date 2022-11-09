# exactly one of them has gone bad
# 只有一瓶奶出问题了
# 但注意，我们不一定能准确地把那一瓶奶找出来
# 尽可能排除，剩下地都当作有毒的

# 排除的方法：
# 把每个生病的人喝的可能有毒的奶找出来
# 有毒的那一瓶一定在小集合里
# 小集合外的一定是好牛奶
# 所以利用n个小集合与大集合做差，尽可能排除



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

person_sickTime = []
for i in range(s):
    person_sickTime.append(list(map(int, input().split())))

# initialize the set
person_milk = {}
for i in range(1, n+1):
    person_milk[i] = set()

# get possible bad milk
possible_bad_milk = set()
for s in person_sickTime:
    for record in person_type_time:
        if record[PERSON] == s[PERSON] \
                and record[TIME] < s[SICK_TIME]:
            possible_bad_milk.add(record[TYPE])
            person_milk[record[PERSON]].add(record[TYPE])

# remove the good milk
for i in person_milk.keys():
    if len(person_milk[i]) > 0:
        good_milk = possible_bad_milk.difference(person_milk[i])
        possible_bad_milk -= good_milk

# count the people
possible_sick_person = set()
for record in person_type_time:
    if record[TYPE] in possible_bad_milk:
        possible_sick_person.add(record[PERSON])


print(len(possible_sick_person))





