a = input('')
counter=0
flag =0
for num in range (1,len(a)):
    if a[num] is a[num - 1]:
        counter+=1
        if counter==6:
            flag+=1
            if flag==1:
                print("YES")
    else:
        counter=0
if flag == 0:
    print('NO')