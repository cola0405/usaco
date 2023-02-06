n = int(input())

one_time = ["MOM", "OOO"]
two_time = ["OOM"]

for r in range(n):
    s = input()
    ans = len(s) - 3

    # 0 time
    if "MOO" in s:
        print(ans)
    elif "MOM" in s or "OOO" in s:
        print(ans+1)
    elif "OOM" in s:
        print(ans+2)
    else:
        print(-1)



