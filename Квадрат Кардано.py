import random
#Квадрат Кардано
a1 = list(input("Введите сообщение (Макс. 16 символов)"))
z=len(a1)
g=len(a1)
res = []
while z<16:
    c=chr(random.randint(65, 89))
    a1+=c
    z+=1
a = ['1','2','3','4']
b = ['5','6','7','8']
c = ['9','10','11','12']
d = ['13','14','15','16']

x = 0
while x<16:
    while x<4:
        if x == 0:
            a[3] = a1[x]
        elif x ==1:
            b[0] = a1[x]
        elif x == 2:
            c[0] = a1[x]
        else:
            d[1] = a1[x]
        x+=1
        
    while x<8:
        if x == 4:
            b[2] = a1[x]
        elif x == 5:
            a[2] = a1[x]
        elif x == 6:
            b[3] = a1[x]
        else:
            a[1] = a1[x]
        x+=1

    while x<12:
        if x == 8:
            a[0] = a1[x]
        elif x == 9:
            b[1] = a1[x]
        elif x == 10:
            c[2] = a1[x]
        else:
            d[3] = a1[x]
        x+=1

    while x<16:
        if x ==12:
            d[0] = a1[x]
        elif x == 13:
            c[1] = a1[x]
        elif x == 14:
            d[2] = a1[x]
        else:
            c[3] = a1[x]
        x+=1
        
    x+=1
    
print(a)
print(b)
print(c)
print(d)

res.append(a[3])
res.append(b[0])
res.append(c[0])
res.append(d[1])
res.append(b[2])
res.append(a[2])
res.append(b[3])
res.append(a[1])
res.append(a[0])
res.append(b[1])
res.append(c[2])
res.append(d[3])
res.append(d[0])
res.append(c[1])
res.append(d[2])
res.append(c[3])

print('Расшифровка -', res[0:g])