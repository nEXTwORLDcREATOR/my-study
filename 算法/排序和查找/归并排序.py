def merge(li,low,mid,high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high: # 只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i+=1
        else:
            ltmp.append(li[j])
            j += 1
    # while 执行完，两部分肯定有一部分没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp


def merge_sort(li,low,high):
    if low < high: # 至少两个元素， 递归
        mid = (low + high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)
        