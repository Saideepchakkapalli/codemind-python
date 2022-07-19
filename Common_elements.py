x , y = map(int,input().split())
l = list(map(int,input().split()))
m = list(map(int,input().split()))
for i in sorted(set(l),key=l.index):
    if m.count(i)!=0:
        print(i,end=" ")