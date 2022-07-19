x = int(input())
l = list(map(int,input().split()))
s=0
for i in l:
    while i!=0:
        v=i%10
        i=i//10
        s+=v
print(s)