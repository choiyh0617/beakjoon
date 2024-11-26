b, p = map(int,input().split())
s=0
while True :
    if b >= 2 and p >= 1 :
        s+= 1
        b-= 2
        p-= 1
    else:
        print(s)
        break