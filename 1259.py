while True:
    result='yes'
    a=input()
    if a=='0':
        break
    for i in range(len(a)//2+1):
        if a[i]!=a[len(a)-1-i]:
            result='no'
            break
    print(result)