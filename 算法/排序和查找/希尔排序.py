def insert_sort_gap(li,gap):
    for i in range(gap,len(li)): #i表示摸到的牌的下标
        tmp = li[i]
        j = i - gap # j 指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li,d)
        d //= 2

li = [3,5,7,3,1,3,5,6,3,2,6]
shell_sort(li)
print(li)