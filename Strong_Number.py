n=int(input())
temp=n
s=0
while temp:
    r=temp%10
    temp//=10
    p=1
    for i in range(r,0,-1):
       p*=i
    s+=p
if s==n:
    print("The number",n,"is a strong number")
else:
     print("The number",n,"is not a strong number")