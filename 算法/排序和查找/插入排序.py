def insert_sort(li):
    for i in range(1,len(li)): #i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1 # j 指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
li = [3,5,7,3,1,3,5,6,3,2,6]
insert_sort(li)
print(li)
