c = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    s = 0
    a = input()
    if a == '#':
        break
    for i in range(len(a)):
        if a[i] in c:
            s += 1
    print(s)