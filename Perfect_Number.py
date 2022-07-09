n=int(input())
x=1
sum=0
while x<=n//2:
    if n%x==0:
        sum+=x
    x+=1
if n==sum:
    print(True)
else:
    print(False)