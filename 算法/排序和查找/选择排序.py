def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new
# 缺点 占内存 。。。。。 o(n**2)

def select_sort(li):
    for i in range(len(li)-1):# i是第几趟
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]
