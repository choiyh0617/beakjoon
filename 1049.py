a, b = map(int, input().split())
pack = []
justone = []
li = []
for i in range(b):
    n, m = map(int, input().split())
    pack.append(n)
    justone.append(m)


li.append(min(pack) * (a // 6) + min(justone) * (a % 6))
li.append(min(pack) * (a // 6 + 1))
li.append(min(justone) * a)

print(min(li))