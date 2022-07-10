n = int(input())
arr = list(map(int,input().split()))
s = 0
for i in range(0,n,2):
    s+=arr[i]
print(s)