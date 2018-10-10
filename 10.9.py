'''
class ly2:
    def __init__(self):  # self 代表初始化类自己 约定熟成用self 啥都行  共享局部变量
        self.suai = 'lalal'#self代表suai是类自身的变量
        self.cou = 'hahaha'
    def fuc(self):
        print(self.suai)
        print(self.cou)
if __name__ == '__main__':
    ly2.fuc()

#ep1
class susu:
    def __init__(self):
        self.su = int(input('输入一个数'))
    def check(self):
        if (self.su % 2) == 0:
    print('偶数')
    else
    print('奇数')

    if __name__ == '__main__':
        susu().check
'''
# class ep2:
#     def __init__(self):
#         self.num = 10
#     def num2(self):
#         self.num=self.num**10
#         if __name__ == '__main__':
#             ep2().num2()
import self

#作业

#1
# class rectangle:
#     def __init__(self,width,heightd):
#         self.width = width
#         self.heightd = heightd
#     def getarea(self):
#             area=self.width * self.heightd
#             print (area)
#     def getzoucang(self):
#             zoucang=self.heightd*2+self.width*2
#             print(zoucang)
# if __name__ == '__main__':
#     rectangle(4,40).getarea()
#     rectangle(4,40).getzoucang()

#2
# class account:
#     def __init__(self,number,balance,annual):
#         self.__id = number
#         self.__balance = balance
#         self.__annualInterestRate = annual
#     def getMonthlyInterestRate(self):
#         res = self.__annualInterestRate / 12
#         return res
#     def getMonthlyInterest(self):
#         res=self.__balance  * self.__annualInterestRate / 12
#         return res
#     def withdraw(self,decrease):
#         self.__balance=self.__balance - decrease
#     def deposit(self,increase):
#         self.__balance=self.__balance + increase
#     def pr(self):
#         print(self.__id,self.__balance,account.getMonthlyInterestRate(self),account.getMonthlyInterest(self))
# account1=account(1122,20000,0.045)
# account1.withdraw(2500)
# account1.deposit(3000)
# account1.pr()


#3
# import math
# class duobianxin:
#     def __init__(self,n,side,x,y):
#         self.__n = n
#         self.__side = side
#         self.__x = x
#         self.__y = y
#     def getPerimeter(self):
#         zoucang =self._duobianxin__side*self._duobianxin__n
#         print(zoucang)
#     def getarea(self):
#         area = (self._duobianxin__n*self._duobianxin__side)/(4*math.tan(3.14/self._duobianxin__n))
#         print(area)
# if __name__ == '__main__':
#     duobianxin(5,6,56,47).getPerimeter()
#     duobianxin(5,6,56,47).getarea()

#4
class fan:
    def __init__(self,speed,kaiguan,radius,color):
        self.__speed = speed
        self.__kaiguan = kaiguan
        self.__radius = radius
        self.__color = color
    def show(self):
        print('[+] speed',self.__speed)
        print('[+] kaiguan',self.__kaiguan)
        print('[+]radius',self.__radius)
        print('[+] color',self.__color)
fan(speed=1,kaiguan='on',radius=8,color='yelow').show()

#5










