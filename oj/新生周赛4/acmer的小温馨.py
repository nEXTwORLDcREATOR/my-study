x,y = map(int,input().split())
total_rmb = x*100 + y*10
game = 1
while True:
    if x==0 and y>=33 or x==1 and y>=23 or x==2 and y >=13 or x>=3 and y>=3:
        if game % 2:
            if x==0:
                y -= 33
            elif x==1:
                x -= 1
                y -= 23
            elif x==2:
                y -= 13
                x -= 2
            else:
                x -= 3
                y -= 3
        else:
            if y>=33:
                y -= 33
            elif y >= 23:
                x -= 1
                y -= 23
            elif y >= 13:
                x -= 2
                y -= 13
            else:
                x -= 3
                y -= 3
        game += 1
    else:
        break
if game % 2 == 0:
    print("Come on,mcq!")
else:
    print("Thank you,lcy~")

