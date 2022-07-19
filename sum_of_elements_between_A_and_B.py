n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
l=[]
c=0
for i in range(n):
    if a[i]>=x and a[i]<=y:
        c=c+a[i]
print(c)