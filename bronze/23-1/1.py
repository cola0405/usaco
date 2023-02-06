# It is guaranteed that there is at least one possible pair.
# 说明必然是有最左边的G或者H覆盖了同种类的所有牛，作 “全覆盖leader”
# 基于这点，再统计覆盖了 ”全覆盖leader“ 的牛的数量即可

n = int(input())
s = input()
e = list(map(int, input().split()))

# leader必然会在左边第一个出现的
first_G_inx = s.find("G")
first_H_inx = s.find("H")

reverse_s = s[::-1]
last_G_inx = len(s)-1 - reverse_s.index("G")
last_H_inx = len(s)-1 - reverse_s.index("H")

G_leader_inx = -1
H_leader_inx = -1

if e[first_G_inx] >= last_G_inx+1:
    G_leader_inx = first_G_inx

if e[first_H_inx] >= last_H_inx+1:
    H_leader_inx = first_H_inx

# 分别统计当G和H分别作”全覆盖leader“时，H和G覆盖到 ”全覆盖leader“的数量
ans = 0
if G_leader_inx != -1:
    for i in range(first_G_inx):
        if (s[i] == "H" and e[i] >= first_G_inx+1) or i == H_leader_inx:
            ans += 1

if H_leader_inx != -1:
    for i in range(first_H_inx):
        if (s[i] == "G" and e[i] >= first_H_inx+1) or i == G_leader_inx:
            ans += 1

print(ans)