import sys
from bisect import *
input = lambda:sys.stdin.readline().strip()
m,n = map(int,input().split())
school_line = list(map(int,input().split()))
stu_s = list(map(int,input().split()))
school_line.sort()
def vs():
    hehe = 0
    for i in stu_s:
        if bisect(school_line, i) == len(school_line):
            s2 = school_line[bisect(school_line,i)-1]
            hehe += abs(s2-i)
        elif bisect(school_line,i) == 0:
            s1 = school_line[bisect(school_line,i)]
            hehe+=abs(s1-i)
        else:
            s1 = school_line[bisect(school_line, i)]
            s2 = school_line[bisect(school_line, i) - 1]
            hehe += min(abs(s1 - i), abs(s2 - i))
    return hehe
ans = vs()
print(ans)