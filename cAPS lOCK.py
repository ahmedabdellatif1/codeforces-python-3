p=0
a=input('')
if len(a)>1:
    if a[0].islower() and a[1:].isupper():
        p+=1
        print(a.capitalize())

    if a.isupper():
        p += 1
        print(a.lower())
if len(a)==1:
    if a[0].islower():
        p += 1
        print(a.upper())
    if a[0].isupper():
        p += 1
        print(a.lower())

if p==0:
    print(a)
