def insert_string(s, index, t):
    return s[:index] + t + s[index:]
s = input()
t = input()
old = t
for i in t:
    if i in s:
        t = t.replace(i,'')
for i in s:
    new = insert_string(s, s.index(i), t)
    if  new == old:
        print(i,t,sep=' ')






















