n=int(input())
s=0
s1=0
a=list(map(int,input().split()))
for i in range(0,n//2):
    s=s+a[i]
for i in range(n//2,n):
    s1=s1+a[i]
print(s)
print(s1)