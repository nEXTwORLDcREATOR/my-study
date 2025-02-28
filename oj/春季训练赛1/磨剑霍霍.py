m,x = map(int,input().split())
goods_list =[0]+[_ for _ in map(int,input().split())]
s = [0]*len(goods_list)
for i in range(1,m+1):
    s[i]=s[i-1]+goods_list[i]
need = []
n = len(str(bin(x))[2:])
if m < n:
    print(sum(goods_list))
else:
    for i in range(n,m+1):
        need.append(s[i]-s[i-n])
    print(max(need))