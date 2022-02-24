print('На каком языке будете писать?')
print('Русский - 1')
print('Англиский - 2')
lang=int(input())
sl=input('Введите сообщение: ')
alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'
alpr='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
a=5
m=4096
y=[0]*len(sl)
y[0]=m-5
chb=[]
сhsl=[]
slcod=[]
sluncod=[]
chsluncod=[]
scslluncod=[]

if lang==1:
    for i in sl:
        chb.append(alpr.index(i)+1)
    for i in range(1, len(sl)):
        y[i]=(a*y[i-1])%m
    for i in range(len(chb)):
        сhsl.append((y[i]+chb[i])%len(alpr))
    for i in сhsl:
        slcod.append(alpr[i])
    sll=''.join(slcod)
    print('Зашифровка - ',sll)
    
    for i in sll:
        chsluncod.append(alpr.index(i))
    for i in range(len(chsluncod)):
        scslluncod.append((chsluncod[i]-y[i])%len(alpr))
    for i in scslluncod:
        sluncod.append(alpr[i-1])
    print('Дешифровка - ',''.join(sluncod))
    
elif lang == 2:
    for i in sl:
        chb.append(alpa.index(i)+1)
    for i in range(1, len(sl)):
        y[i]=(a*y[i-1])%m
    for i in range(len(chb)):
        сhsl.append((y[i]+chb[i])%len(alpa))
    for i in сhsl:
        slcod.append(alpa[i])
    sll=''.join(slcod)
    print('Зашифровка - ',sll)
    
    for i in sll:
        chsluncod.append(alpa.index(i))
    for i in range(len(chsluncod)):
        scslluncod.append((chsluncod[i]-y[i])%len(alpa))
    for i in scslluncod:
        sluncod.append(alpa[i-1])
    print('Дешифровка - ',''.join(sluncod))
else:
    print('Язык выбран неправильно!')