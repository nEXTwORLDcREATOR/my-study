def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            #987 it=1 987//10 -> 98 98%10->8;  it=2 987//100->9 9%10=9
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        #分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        #把数字重新写回li
        it += 1

# import random
# li = list(range(1000))
# random.shuffle(li)
# radix_sort(li)
# print(li)
