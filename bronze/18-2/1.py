import sys
sys.stdin = open("teleport.in","r")
sys.stdout = open("teleport.out","w")

start,end,t1,t2 = map(int, input().split())

# no teleport
ans = abs(start - end)

# go teleport
way1 = abs(start - t1) + abs(end - t2)
way2 = abs(start - t2) + abs(end - t1)

ans = min(ans, way1, way2)
print(ans)


