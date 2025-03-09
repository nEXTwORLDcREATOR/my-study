dirs = [lambda x,y:(x+1,y),
        lambda x,y:(x,y+1),
        lambda x,y:(x-1,y),
        lambda x,y:(x,y-1),
        lambda x,y:(x-1,y-1),
        lambda x,y:(x-1,y+1),
        lambda x,y:(x+1,y-1),
        lambda x,y:(x+1,y+1)]

N,M = map(int,input().split())
spider = []
for i in range(N):
    spider.append(list(input()))

def is_vaild(x,y):
    return  0<= x <N and 0<= y < M

def clean_water(x,y):
    start = (x,y)
    spider[x][y] = "n"
    for dir in dirs:
        nextcode = dir(start[0], start[1])
        if is_vaild(nextcode[0],nextcode[1]):
            if spider[nextcode[0]][nextcode[1]] == "W":
                clean_water(nextcode[0],nextcode[1])

water_num = 0
for i in range(N):
    for j in range(M):
        if spider[i][j] == "W":
            water_num += 1
            clean_water(i,j)

print(water_num)
