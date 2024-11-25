def friend () :
    n,m = map(int,input().split())
    if n!=0 and m!=0:
        print(n+m)
        friend()

friend()