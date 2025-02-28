def sift(li,low,high): #li:列表 low:堆的根节点位置 high:堆的最后一个元素的位置
    i = low # i 最开始指向根节点
    j = 2 * i + 1 # j开始是左孩子
    tmp = li[low] # 把堆顶存起来
    while j <= high : # 只要j位置有数
        if j + 1 <= high and li[j+1] > li[j]: # 如果右孩子有并且比较大
            j = j + 1 # j指向右孩子
        if li[j] > tmp:
            li[i] = li [j]
            i = j           # 往下看一层
            j = 2 * i + 1
        else:             # tmp 更大，把tmp放到i的位置上
            li[i] = tmp      # 把tmp放到某一级领导位置上
            break
    else:
        li[i] = tmp   # 把tmp放到叶子节点上

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):
        # i 表示建堆的时候调整的部分的根的下标
        sift(li,i,n-1)
    # 建堆完成了
    for i in range(n-1,-1,-1):
        # i 指向当前堆的最后一个元素
        li[0],li[i] = li[i],li[0]
        sift(li,0,i-1) # i-1是新的high

# li = [i for i in range(100)]       o(nlogn)
# import random
# random.shuffle(li)
# heap_sort(li)
# print(li)


