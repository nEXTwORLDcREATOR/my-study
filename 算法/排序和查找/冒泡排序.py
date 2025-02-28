def bubble_sort(li):
    for i in range(len(li)-1): # 第i趟
        exchange = False
        for j in range(len(li)- i - 1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        # print(li)
        if not exchange:
            return
list1 = [54,26,93,17,77,31,44,55,20]
bubble_sort(list1)
print(list1)
# 一趟排序没有发生交换 ，即可认为已经排好



