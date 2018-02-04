a = input('')
n = int(input(''))
b=[0]
c=[]
count = 0
for i in range (1,len(a)):
    if a[i] is a[i-1] :
        count += 1
        b.append(count)
    elif a[i] is not a[i-1]:
        b.append(count)
for _ in range(n):
    a = [int(x) for x in input().split()]

    v=b[a[1]-1]-b[a[0]-1]
    c.append(v)
for elements in c:
    print(elements)






