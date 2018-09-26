'''
r = eval(input(">>"))  #1
s = 2*r*0.58
area = 5*s*s/(4*0.72)
print(area)

import math  #2
x1,y1 = eval(input(">>"))
x2,y2 = eval(input(">>"))
d = 6371.01*math.acos(math.sin(math.radians(x2))*math.sin(math.radians(x1))+math.cos(math.radians(x1))*math.cos(math.radians(y1)-math.radians(y2)))
print(d)



import math # 3
s = eval(input('>>'))
sang = 5*s*s
xia = 4*math.tan(3.14/5)
area = sang/xia
print(area)



import math  #4
s = eval(input(">>"))
n = eval(input(">>"))
area = (n*s**2)/(4*math.tan(3.14/n))
print(area)



num = eval(input(">>")) #5
asc = chr(num)
print(asc)



xm = (input(">>")) #6
gzsj = eval(input(">>"))
mxsbc = eval(input(">>"))
lbsl = eval(input(">>"))
zsl = eval(input(">>"))
sq = gzsj*mxsbc
sh = sq-sq*lbsl-sq*zsl
print('name:',xm)
print('gross pay:',sq)
print('net pay:',sh)



x = int(input(">>")) #7
a = int(x/1000%10)
b = int(x/100%10)
c = int(x/10%10)
d = int(x%10)
e = d*1000+c*100+b*10+a
print(e)


x = input(">>") #7
y = x[::-1]
print(y)



import math  #1
a,b,c = eval(input(">>"))
p = b*b-4*a*c
if p>0 and a!=0:
    x1=(-b+math.sqrt(p))/(2*a)
    x2=(-b-math.sqrt(p))/(2*a)
elif a==0:
    x1 = x2 = -c / b
else:
    print('no jie')

print(x1,x2)



import random #2
num1 = random.randint(0,99)
num2 = random.randint(0,99)
he = num1+num2
x = int(input(">>"))
if x==he:
    print('ture')
else:
    print('false')


a,b = eval(input(">>"))  #3
for i in range(0,7):
    if(a==i):
        c=(b-7+a)%7
        print('today is {} and future is {} ',a,c)
    else:
        print('xx')

'''

a,b,c = eval(input(">>"))
if a<b:
    a,b=b,a
if a<c:
    a,c=c,a
if b<c:
    b,c=c,b
print(c,b,a)






