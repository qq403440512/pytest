'''
i = 0
while i<10:
    i += 1
    print('good')

i=0
for i in 'abcgd':
    print(i)

a= 'abcgd'
i = 0
while i<5:
    print(a[i])
    i+=1


import random
sjs = random.randint(0,10)
su =eval(input('>>'))
while su!=sjs:
    if su>sjs:
        print("you big")
        su = eval(input('>>'))

    if su<sjs:
        print("you little")
        su = eval(input('>>'))

while su==sjs:
    print("you are right")
    break
sun = 0
for i in range(1001):
sum = sum + 1


sun = 0
i=0
while i<1001:
    sun+=i
i +=1

def hotcold(c):
    hasi = c*9/5+32
    return str(hasi)+'F'
ctf = hotcold(35)
print(ctf)




for i in range(1,10):
     for j in range(1,i+1):
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
print (" ")


for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(j,i,i*j),end=' ')
    print()


def test2(name):
    print(name)
    test2('joker')

def fun1():
    print('hahaha')
    return 100,122,1222
# return None
a = fun1()
print(a)

def fun1(num1,num2):
    return num1,num2
def fun2(num1,num2):
    num11 = num1**2
    num22 = num2**2
    return num11,num22
def fun3(num1,num2,num3,num4):
    res1 = num1+num2
    res2 = num3+num4
    print(res1,res2)

a,b=fun1(1,2)
c,d= fun2(a,b)
fun3(a,b,c,d)



num = float(input(">>"))  #1
zs=0
fs=0
i1=0
i2=0
while (num!=0):
    if num>0:
        zs+=1
        i1=i1+num
        num = float(input(">>"))
    else:
        fs+=1
        i2=i2+num
        num = float(input(">>"))
pjs = (i1+i2)/ (zs + fs)
print(zs,fs,pjs)


csxf=10000  #2
xf10=csxf*(1+0.05)**10
sum=0
for i in  range (10,14):
    sum = sum + csxf*(1+0.05)**i
    i+=1
print(xf10,sum)

j=0
for i in range (100,1001): #3
    if(i%5==0 and i%6==0):
        print(i,end=" ")
        j+=1
        if(j==10):
            print(end='\n')


i=1           #5
q=100
while i**2>12000:
    i+=1
i=i*-1
print(i)
while q**3<12000:
    q-=1
print(q)

'''
for i in range(1,8):
    print(i,end=" ")
    for o in  range(1,8):
        print(o,end=' ')





















