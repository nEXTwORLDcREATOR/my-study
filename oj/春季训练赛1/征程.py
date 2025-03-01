n = int(input())
monster_list = [i for i in input().split()]
monster_list.sort()
def dfs(index,li,group,result):
    if index == len(li):
        if group:
            result.append(group)
        return result
    dfs(index+1,li,group+li[index],result)
    dfs(index+1,li,group,result)
result = []
dfs(0,monster_list,"",result)
result.sort()
for i in result:
    print(i)

