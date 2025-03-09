import sys
input = lambda:sys.stdin.readline().strip()
a,b,c,d = map(float,input().split())
def check(x):
    return a*x**3+b*x**2+c*x+d
def bisect(lo,hi):
    while abs(lo - hi) > 1e-7:
        mid = (lo + hi) / 2
        if check(mid) == 0:
            return mid
        elif check(lo)*check(mid) < 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2
ans = []
for i in range(-100,101):
    l = i
    r = i+1
    if check(l) == 0:
        ans.append(l)
    elif check(r) == 0:
        ans.append(r)
    elif check(l)*check(r) < 0:
        ans.append(bisect(l,r))
    if len(set(ans)) == 3:
        break

a1 = set(ans)
a2 = list(a1)
a2.sort()
for i in a2:
    print(f"{i:.2f}",end=" ")