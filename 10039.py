c=0
for i in range(5):
    n=int(input())
    if n<40:
        c+=40
    else:
        c+=n
print(c//5)