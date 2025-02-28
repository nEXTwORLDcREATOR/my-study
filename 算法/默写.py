# 选择排序
'''
def select_sort(li):
    for i in range(len(li)-1):
        min_local = i
        for j in range(i+1,len(li)):
            if li[min_local] > li[j]:
                min_local = j
        li[j],li[min_local] = li[min_local],li[j]
'''

# 冒泡排序
'''
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange =  True
            else:
                return
        print(li)
list1 = [9,8,7,6,5,4,3,2,1]
bubble_sort(list1)
print(list1)
'''

# 二分查找
'''
def binary_search(li,val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left+right)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 
    else:
        return None
'''

# 插入排序
'''
def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i -1
        while j >= 0 and li[j]>tmp:
            li[j+1] = li[j] #赋值从右向左
            j -= 1
        li[j+1] = tmp
li = [2,3,5,7,8,5,6,3,5,7]
insert_sort(li)
print(li)
'''

# 快速排序
'''
def partition(li,left,right):
    tmp = li[left]
    while left < right :
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return right
def quick_sort(li,left,right):
    if left < right:
        mid = partition(li,left,right)
        quick_sort(li,left,mid - 1)
        quick_sort(li,mid+1,right)
'''





