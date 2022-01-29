#Шифр Гронсфельда
s1=input('Введите сообщение ')
s2=''
s4=''
s3=input('Введите ключ ')
sm=[]
sm+=s3
n=0
nn=0
so=[]
print('Сообщение состоит из', len(s1), 'символов')
for i in  range(0,(len(s1)-len(sm))):
    sm+=sm[n]
    n+=1
print('Введен ключ: ', sm)
print('Ключ имеет',len(sm), 'символов')
for i in range(len(s1)):
    so.append(sm[nn])
    nn+=1
    zn=''.join(so)
    if ord(s1[i])<4000:                      #Эта часть 
        s2=s2+chr(ord(s1[i])+(int(zn)))      #взята из 
    else:                                    #кода Цезаря 
        s2=s2+chr(ord(s1[i])+(int(zn))-4000) #в документе лабы
    so=[]
print('Зашифровка - ', s2)
nn=0
zn=0
for i in range(len(s1)):
    so.append(sm[nn])
    nn+=1
    zn=''.join(so)
    if ord(s1[i])<4000:
        s4=s4+chr(ord(s1[i])-(int(zn)))
    else:
        s4=s4+chr(ord(s1[i])-(int(zn)+4000))
    so=[]
print('Дешифровка - ', s4)

