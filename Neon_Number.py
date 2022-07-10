t = int(input())
s = t*t
a = 0
while s:
    a += s%10
    s//=10
if a==t:
    print("Neon Number")
else:
    print("Not Neon Number")