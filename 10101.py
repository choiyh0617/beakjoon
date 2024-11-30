a=int(input())
b=int(input())
c=int(input())
if a==b==c==60:
    print("Equilateral")
else:
    if a+b+c != 180:
        print("Error")
    else:
        if a==b==60 or b==c==60 or c==a==60:
            print('Isosceles')
        else:
            print('Scalene')