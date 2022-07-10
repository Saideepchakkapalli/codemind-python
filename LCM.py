a,b = map(int,input().split())
for i in range(1,100):
    if a*i%b==0:
        print(a*i)
        break