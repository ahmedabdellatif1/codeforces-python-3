n = int(input(''))
c=[]
f=[]
for _ in range(n):
    a = [int(x) for x in input().split()]
    c.extend(a)
for elements in c:
    f.append(elements)
sm1 = sum(f[0:len(f):3])
sm2 = sum(f[1:len(f):3])
sm3 = sum(f[2:len(f):3])
if sm1 == sm2 == sm3 ==0:
    print("YES")
else:

    print("NO")

