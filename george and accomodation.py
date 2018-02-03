n = int(input(''))
c=0
for _ in range(n):
    a = [int(x) for x in input().split()]
    if a[1]>(a[0]+1):
        c=c+1

print(c)