vowels=['a','e','i','o','u']
s=input()
d=[]
for i in vowels:
    if i not in s:
        d.append(i)
if len(d)==0:
    print('0')
else:
    print(*d)
