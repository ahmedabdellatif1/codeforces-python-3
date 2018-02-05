v=[]
a= input('')
c=a.lower()
for word in c:
    Vowels = 'aiueoy'
    for i in range (0,len(Vowels)):
        word = word.replace(Vowels[i],'')
    if len(word)>0:
        v.append('.')
        v.append(str(word))
print(''.join(v))

