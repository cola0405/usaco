# 60%
# person 2 didn't drink milk 4 but still got sick
# so the bad milk is 1 or 2, not 1 2 4

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

# avoid over count
possible_bad_milk = set()
for s in person_sickTime:
    for record in person_type_time:
        if record[PERSON] == s[PERSON] \
                and record[TIME] < s[SICK_TIME]:
            possible_bad_milk.add(record[TYPE])

possible_sick_person = set()
for record in person_type_time:
    if record[TYPE] in possible_bad_milk:
        possible_sick_person.add(record[PERSON])

print(len(possible_sick_person))





