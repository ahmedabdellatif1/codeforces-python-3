n = int(input(''))
c=[]
for _ in range(n):
    a = input('')
    if len(a)<=10:
        c.append(a)

    else:
        c.append(a[0]+str(len(a)-2)+a[len(a)-1])

for words in c :
    print(words)