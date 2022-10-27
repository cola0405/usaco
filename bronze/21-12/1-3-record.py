# 超时


# GGHHGG

# HHHGHHH

# HHHHGHH
# 与HG的数量没直接关系
# 但是，跟G的位置是有关系的
# 所以这种记录的方式是行不通的（或者说你还要记录位置信息，很麻烦了）

n = int(input())
s = list(input())
ans = 0

G = []
H = []
lonely_photo = []


g = 0
h = 0
t = 0
for i in range(n):
    if s[i] == 'G':
        g += 1
    else:
        h += 1
    if h > 1 and g > 1:
        if h <= g:
            h -= 1
        else:
            g -= 1
        break
    if h + g >= 3 and (g == 1 or h == 1):
        t += 1
ans += t
G.append(g)
H.append(h)
lonely_photo.append(t)

for i in range(1, n):
    g = G[i - 1]
    h = H[i - 1]
    if s[i-1] == 'G':
        g -= 1
    else:
        h -= 1
    if g == 0 or h == 0 or g+h < 3:
        t = 0
    else:
        t = lonely_photo[i-1]
    for j in range(i+g+h, n):
        if s[j] == 'G':
            g += 1
        else:
            h += 1
        if h > 1 and g > 1:
            if s[j] == 'H':
                h -= 1
            else:
                g -= 1
            break
        if h + g >= 3 and (g == 1 or h == 1):
            t += 1
    ans += t
    G.append(g)
    H.append(h)
    lonely_photo.append(t)
    #print(ans)

print(ans)
#print(lonely_photo)




