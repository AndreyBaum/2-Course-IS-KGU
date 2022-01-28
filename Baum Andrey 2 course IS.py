#Шифр Гронсфельда
s1=input('Введите сообщение (на английском) ')
s2=''
s3=input('Введите ключ ')
sm=[]
sm+=s3
n=0
nn=0
so=[]
for i in  range(0,(len(s1)-len(sm))):
    sm+=sm[n]
    n+=1
print(sm)
for i in range(len(s1)):
    so.append(sm[nn])
    nn+=1
    zn=''.join(so)
    if ord(s1[i])<253:
        s2=s2+chr(ord(s1[i])+(int(zn)))
    else:
        s2=s2+chr(ord(s1[i])+(int(zn))-255)
    so=[]
print(s2)
print(s1)

