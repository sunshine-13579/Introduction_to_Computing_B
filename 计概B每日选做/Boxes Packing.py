n=int(input())
a=list(map(int,input().split()))
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(max(b.values()))