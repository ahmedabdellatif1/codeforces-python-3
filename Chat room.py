st = input('')
def solve(st):
    word = "hello"
    index = 0
    for i in range(0,len(st)):
        if(index==5):
            return "YES"
        if(st[i]==word[index]):
            index+=1

    if(index<5):
        return "NO"
    else:
        return "YES"



print (solve(st))











