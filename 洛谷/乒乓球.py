list1 = []
s = ""
while True:
    tmp = input()
    s += tmp
    if 'E' in tmp:
        break
for i in s:
    list1.append(i)
a = list1.index('E')
list1 = list1[:a]
n = len(list1)
w = 0
l = 0
for i in list1:
    if i == 'W':
        w += 1
        n -= 1
    elif i =='L':
        l += 1
        n -= 1
    if abs(w-l)>=2 and (w >= 11 or l >= 11):
        print(w,':',l,sep="")
        w = 0
        l = 0
    elif n + w + l < 11 and n == 0:
        print(w,':',l,sep="")
        break
print()
w = 0
l = 0
n = len(list1)
for j in list1:
    if j == 'W':
        w += 1
        n -= 1
    elif j == 'L':
        l += 1
        n -= 1
    if abs(w-l)>=2 and (w >= 21 or l >= 21):
        print(w,':',l,sep="")
        w = 0
        l = 0
    elif n + w +l < 21 and n == 0:
        print(w,':',l,sep="")
        break