n = int(input())
s=1
if n == 0 :
    print(1)
else :
    for i in range(n, 1, -1):
        s = n * s
        n = n-1
    print(s)