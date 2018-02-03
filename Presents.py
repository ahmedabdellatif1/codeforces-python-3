
c = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

b=[]

for x in range(1,max(a)+1):


    b.insert((x)-1, a.index(x)+1)
for elements in b:
    print(elements)



