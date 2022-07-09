def l_pal(n):
    while n:
        rev = 0
        temp = n
        while temp:
            rev=rev*10+temp%10
            temp//=10
        if rev==n:
            return rev
        n-=1    
    
def r_pal(n):
    while n:
        rev = 0
        temp = n
        while temp:
            rev=rev*10+temp%10
            temp//=10
        if rev==n:
            return rev
        n+=1
    
n = int(input())
l = l_pal(n-1)
r = r_pal(n+1)
if n-l<r-n:
    print(l)
elif n-l>r-n:
    print(r)
else:
    print(l,r)