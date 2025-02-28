def count_sort(li,max_count = 100):
    count = [0 for _ in range(max_count+1) ]
    for val in li:
        count[val] += 1
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)

# list1 = [1,3,54,2,5,21,54,2,3,5,2,1,2]
# count_sort(list1)
# print(list1)