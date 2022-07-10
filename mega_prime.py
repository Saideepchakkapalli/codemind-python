def is_prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        return 1
        
n = int(input())
d = 0
p = 0
if is_prime(n):
    while n:
        if is_prime(n%10):
            p += 1
        d += 1
        n//=10
    if d==p:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")