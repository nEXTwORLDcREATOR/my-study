m,x = map(int,input().split())
goods_price = [i for i in map(int,input().split())]
if x >= sum(goods_price):
    print(m)
else:
    left = 0
    max_sum = 0
    for right in range(m):
        x -= goods_price[right]
        while x < 0:
            x += goods_price[left]
            left += 1
        max_sum = max(max_sum, right - left+1)
    print(max_sum)