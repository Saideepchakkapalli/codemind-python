s=input()
s=s.split(":")
h=int(s[0])
if h>12:
    h-=12
    if h<10:
        print('0',end='')
    print(h,s[1],sep=':',end=' ')
    print('PM')
elif h<12 and h>0:
    if h<10:
        print('0',end='')
    print(h,s[1],sep=':',end=' ')
    print('AM')
elif h==12:
    print(h,s[1],sep=':',end=' ')
    print('PM')
elif h==0:
    h+=12
    print(h,s[1],sep=':',end=' ')
    print('AM')