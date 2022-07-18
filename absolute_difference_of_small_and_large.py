s=input().split()
for i in s:
    maxi=ord(max(i))
    mini=ord(min(i))
    print(maxi-mini,end=' ')